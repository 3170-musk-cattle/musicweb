from django.db import models

# Create your models here.
#

prov_choices = [
    ('AH', 'Anhui'),
    ('BJ', 'Beijing'),
    ('FJ', 'Fujian'),
    ('GS', 'Gansu'),
    ('GD', 'Guangdong'),
    ('LN', 'Liao Ning'),
]

class Songs(models.Model):
    name = models.CharField(max_length=511)
    genre = models.ForeignKey('Genres', on_delete=models.SET_NULL, null=True, blank=True)
    artist = models.ForeignKey('Artists', on_delete=models.CASCADE)
    album = models.ForeignKey('Albums', on_delete=models.CASCADE)
    file_name = models.URLField(max_length=511, null=True, blank=True)
    story = models.TextField(max_length=2047)
    time_played = models.IntegerField()
    time_played_full = models.IntegerField()
    lyric = models.TextField(max_length=2047)
    class Meta:
        unique_together = ('name', 'artist', 'album')


class Artists(models.Model):
    name = models.CharField(max_length=255, db_index=True, unique=True)
    introduction = models.TextField(max_length=2047)


class Albums(models.Model):
    name = models.CharField(max_length=255)
    artist = models.ForeignKey('Artists', on_delete=models.CASCADE)
    publish_date = models.DateField()

    class Meta:
        unique_together = ('name', 'artist')


class RankLists(models.Model):
    name = models.CharField(max_length=255)
    create_date = models.DateField(auto_now_add=True)

class Genres(models.Model):
    name = models.CharField(verbose_name='Genre Name', max_length=20, db_index=True, primary_key=True)
    rank_list = models.ForeignKey('RankLists', on_delete=models.SET_NULL, null=True, blank=True)

class RankListSong(models.Model):
    list_id = models.ForeignKey('RankLists', on_delete=models.CASCADE)
    song_id = models.ForeignKey('Songs', on_delete=models.CASCADE)
    rank_index = models.PositiveIntegerField()

    class Meta:
        unique_together = ('list_id', 'song_id')

class PlayLists(models.Model):
    name = models.CharField(max_length=50)
    create_usr = models.ForeignKey('Users', on_delete=models.SET_NULL, null=True, blank=True)
    create_date = models.DateField(auto_now_add=True)


class Reviews(models.Model):
    user_id = models.ForeignKey('Users', on_delete=models.SET_NULL, null=True, blank=True)
    song_id = models.ForeignKey('Songs', on_delete=models.CASCADE)
    content = models.TextField()
    comment_date = models.DateField()


class Users(models.Model):
    name = models.CharField(max_length=50)
    create_date = models.DateField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now=True)
    password = models.CharField(max_length=255)
    gender = models.CharField(
        max_length=2,
        choices=[
            ('M', 'Male'), 
            ('F', 'Female')
            ('N', 'Unknown')
        ], default='N'
    )
    location = models.CharField(
        max_length=20,
        choices=prov_choices,
        default='GD'
    )
    email_address = models.EmailField(unique=True, primary_key=True)
    like_songs = models.ForeignKey(PlayLists, on_delete=models.PROTECT)



class ArtistInGroup(models.Model):
    group_id = models.ForeignKey('Artists', on_delete=models.CASCADE, related_name='group')
    artist_id = models.ForeignKey('Artists', on_delete=models.CASCADE, related_name='single')

    class Meta:
        unique_together = ('group_id', 'artist_id')


class UserPlaysMusic(models.Model):
    user_id = models.ForeignKey('Users', on_delete=models.CASCADE)
    song_id = models.ForeignKey('Songs', on_delete=models.CASCADE)
    last_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user_id', 'song_id')


class PlaylistSong(models.Model):
    list_id = models.ForeignKey('PlayLists', on_delete=models.CASCADE)
    song_id = models.ForeignKey('Songs', on_delete=models.CASCADE)
    add_date = models.DateTimeField()

    class Meta:
        unique_together = ('list_id', 'song_id')





class UserLikePlaylist(models.Model):
    user_id = models.ForeignKey('Users', on_delete=models.CASCADE)
    list_id = models.ForeignKey('PlayLists', on_delete=models.CASCADE)

    class Meta:
        unique_together = ('list_id', 'user_id')

class UserIsFanOf(models.Model):
    user_id = models.ForeignKey('Users', on_delete=models.CASCADE)
    artist_id = models.ForeignKey('Artists', on_delete=models.CASCADE)
    add_time = models.DateTimeField(auto_created=True)
    class Meta:
        unique_together = ('user_id', 'artist_id')
    
class Reviews(models.Model):
    user_id = models.ForeignKey('Users', on_delete=models.SET_NULL, null=True, blank=True)
    song_id = models.ForeignKey('Songs', on_delete=models.CASCADE)
    comment = models.TextField(max_length=2047)
    comment_date = models.DateTimeField(auto_created=True)




