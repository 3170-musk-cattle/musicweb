from django.shortcuts import render
from django.http import JsonResponse
from oxygen.data import *
import json

# Create your views here.
def view_something(request):
    data = {
        'code': 0,
        'name': 'abaaba',
    }
    return JsonResponse(data)


def insert_db(request):
    response = {
        'msg': 'insert done.'
    }
    path = '/home/jdr/Downloads/QQM/QM/music.json'
    file = open(path, 'r')
    for raw_json in file:
        song_info = json.loads(raw_json)
        new_song(
            song_info['song_name'],
            get_genre(song_info['song_type']),
            '/'.join(sorted(song_info['singer_name'])),
            song_info['album_name'],
            song_info.get('lyric', ''),
            song_info['song_time_public'],
            0,0,'',
            song_info['song_url']
        )
    file.close()
    return JsonResponse(response)
