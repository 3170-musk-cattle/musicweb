from django.shortcuts import render
from django.http import JsonResponse
from django.core import serializers

from hydrogen.models import *

import json


# Create your views here.

def get_genre(genre_idx):
    if genre_idx == 93:
        return 'light music'
    if genre_idx == 44:
        return 'traditional'
    return [
        '', '', 'electronic', 'rap', 'rock',
        '', 'heavy metal', 'pop', 'folk music', '',
        'blues', 'R&B', '', 'country', 'jazz',
        '新世界', '', '', '', 'guofeng',
        'ethnic'
    ][genre_idx]


def add_user(request):
    response = {}
    try:
        userinfo = {
            'name': request.GET.get('user_name'),
            'password': request.GET.get('password'),
            'email_address': request.GET.get('email')
        }
        user = Users(**userinfo)
        user.save()
        response['msg'] = 'success'
        response['err_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['err_num'] = 1

    return JsonResponse(response)


def show_users(request):
    response = {}
    try:
        users = Users.objects.filter()
        response['list'] = json.loads(serializers.serialize('json', users))
        response['msg'] = 'success'
        response['err_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['err_num'] = 1
    return JsonResponse(response)


def show_songs(request):
    response = {}
    try:
        songs = Songs.objects.filter()
        response['list'] = json.loads(serializers.serialize('json', songs))
        response['msg'] = 'success'
        response['err_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['err_num'] = 1
    return JsonResponse(response)


def add_song(request):
    response = {}
    try:
        song_info = {
            'name': request.GET.get('song_name'),
            'genre': request.GET.get('genre'),
            'artist': request.GET.get('artist'),
            'album': request.GET.get('album'),
            'file_name': request.GET.get('path'),
            'length': request.GET.get('duration'),
        }
        song = Songs(**song_info)
        song.save()
        response['msg'] = 'success'
        response['err_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['err_num'] = 1
    return JsonResponse(response)


def add_artist(request):
    response = {}
    try:
        artist_info = {
            'name': request.GET.get('name'),
        }
        artist = Artists(**artist_info)
        artist.save()
        response['msg'] = 'success'
        response['err_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['err_num'] = 1
    return JsonResponse(response)


def show_artists(request):
    response = {}
    try:
        artists = Artists.objects.filter().order_by('name')
        print(serializers.serialize('json', artists))
        response['list'] = json.loads(serializers.serialize('json', artists))
        # for key, item in response.items():
        #     item[]
        response['msg'] = 'success'
        response['err_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['err_num'] = 1
    return JsonResponse(response)


def delete_artist(request):
    response = {}
    try:
        Artists.objects.filter(name=request.GET.get('pk')).delete()
        response['msg'] = 'success'
        response['err_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['err_num'] = 1
    return JsonResponse(response)


def register_songs_from_file(request):
    response = {}
    try:
        cnt = 0
        path = request.GET.get('path')
        print(path)
        with open(path, 'r') as file:
            for raw_json in file:
                print(raw_json)
                song_info = json.loads(raw_json)
                artists = song_info['singer_name']
                for artist in artists:
                    artist_info = Artists.objects.filter(name=artist)
                    if not artist_info.exists():
                        new_artist = Artists(name=artist)
                        new_artist.save()

                group = '/'.join(sorted(artists))
                group_info = Artists.objects.filter(name=group)
                print(group)
                if not group_info.exists():
                    new_group = Artists(name=group)
                    new_group.save()
                    for artist in artists:
                        ArtistInGroup(group_id=new_group, artist_id=Artists.objects.get(name=artist)).save()
                print(song_info['album_name'])
                album_info = {
                    'name': song_info['album_name'],
                    'artist': Artists.objects.get(name=group)
                }

                if not Albums.objects.filter(**album_info).exists():
                    new_album = Albums(publish_date=song_info['song_time_public'], **album_info)
                    new_album.save()
                album = Albums.objects.get(**album_info)
                artist = Artists.objects.get(name=group)
                name = song_info['song_name']

                genre_info = get_genre(int(song_info['song_type']))
                if not Genres.objects.filter(name=genre_info).exists():
                    genre_rank = RankLists(name='Top '+genre_info.title())
                    genre_rank.save()
                    new_genre = Genres(name=genre_info, rank_list=genre_rank)
                    new_genre.save()
                genre = Genres.objects.get(name=genre_info)
                if not (Songs.objects.filter(name=name, artist=artist, album=album).exists()):
                    song_data = {
                        'name': name,
                        'genre': genre,
                        'artist': artist,
                        'album': album,
                        'file_name': song_info['song_url'],
                    }
                    new_song = Songs(**song_data)
                    new_song.save()
                    cnt += 1
        response['msg'] = 'success'
        response['err_num'] = 0
        response['cnt'] = cnt
    except Exception as e:
        response['msg'] = str(e)
        response['err_num'] = 1
    return JsonResponse(response)


def show_songs(request):
    response = {}
    try:
        songs = Songs.objects.filter()
        response['list'] = json.loads(serializers.serialize('json', songs))
        response['msg'] = 'success'
        response['err_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['err_num'] = 1
    return JsonResponse(response)
