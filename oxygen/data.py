from oxygen.models import *


def get_genre(genre_idx):
    if genre_idx == 93:
        return 'light music'
    if genre_idx == 44:
        return 'traditional'
    return [
        'pop', '', 'electronic', 'rap', 'rock',
        '', 'heavy metal', 'pop', 'folk music', '',
        'blues', 'R&B', '', 'country', 'jazz',
        '新世界', '', '', '', 'guofeng',
        'ethnic'
    ][genre_idx]

def register_into_group(group_id, artist_id):
    if ArtistInGroup.objects.filter(group_id=group_id, artist_id=artist_id).exists():
        return ArtistInGroup.objects.get(group_id=group_id, artist_id=artist_id)
    relation = ArtistInGroup(
        group_id=group_id,
        artist_id=artist_id
    )
    relation.save()
    return relation

def new_artist(name: str, introduction='no records'):
    if Artists.objects.filter(name=name).exists():
        return Artists.objects.get(name=name)
    if '/' in name:
        artists = [new_artist(a_name) for a_name in name.split('/')]
        group = Artists(name=name, introduction=introduction)
        group.save()
        for artist in artists:
            register_into_group(group, artist)
        return group
    artist = Artists(name=name, introduction=introduction)
    artist.save()
    return artist

def new_album(name, publish_date, artist_name):
    artist = new_artist(artist_name)
    if Albums.objects.filter(name=name, artist=artist).exists():
        return Albums.objects.get(name=name, artist=artist)
    album = Albums(name=name, publish_date=publish_date, artist=artist)
    album.save()
    return album

def new_genre(name):
    if Genres.objects.filter(name=name).exists():
        return Genres.objects.get()
    ranklist = RankLists(name = f'Top of {name}')
    ranklist.save()
    genre = Genres(name=name, rank_list=ranklist)
    genre.save()
    return genre

def new_song(name, genre_name, artist_name, album_name, lyric, publish_time='2021-01-21', time_played=0, time_played_full=0, story='', file_name = ''):
    if publish_time == '0000-00-00' or publish_time=='':
        publish_time = '2000-01-01'
    info_unique = {
        'name':     name,
        'artist':   new_artist(artist_name),
        'album':    new_album(album_name, publish_date=publish_time, artist_name=artist_name)
    }
    if Songs.objects.filter(**info_unique).exists():
        return Songs.objects.get(**info_unique)
    song = Songs(
        name=name,
        genre=new_genre(genre_name),
        artist=info_unique['artist'],
        album=info_unique['album'],
        file_name=file_name,
        story=story,
        time_played=time_played,
        time_played_full=time_played_full,
        lyric=lyric
    )
    song.save()
    return song

