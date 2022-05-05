from django.db import models


# Create your models here.

class Songs(models.Model):
    name = models.CharField(max_length=255)
    genre = models.ForeignKey('Genres', on_delete=models.SET_NULL, null=True, blank=True)
    artist = models.ForeignKey('Artists', on_delete=models.CASCADE)
    album = models.ForeignKey('Albums', on_delete=models.CASCADE)
    file_name = models.URLField(max_length=255, null=True, blank=True)
    length = models.PositiveIntegerField(null=True, blank=True, default=0)  # unit: second, the length of music

    class Meta:
        unique_together = ('name', 'artist', 'album')


class Artists(models.Model):
    name = models.CharField(max_length=50, db_index=True, unique=True)


class Albums(models.Model):
    name = models.CharField(max_length=50)
    artist = models.ForeignKey('Artists', on_delete=models.CASCADE)
    publish_date = models.DateField()

    class Meta:
        unique_together = ('name', 'artist')


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
    email_address = models.EmailField(unique=True, primary_key=True, db_index=True)

    # New Feature
    # like_songs = models.ForeignKey(PlayLists)


class RankLists(models.Model):
    name = models.CharField(max_length=50)
    create_date = models.DateField(auto_now_add=True)


class Genres(models.Model):
    name = models.CharField(verbose_name='Genre Name', max_length=20, db_index=True, primary_key=True)
    rank_list = models.ForeignKey('RankLists', on_delete=models.PROTECT)


class UserPlaysMusic(models.Model):
    user_id = models.ForeignKey('Users', on_delete=models.CASCADE)
    song_id = models.ForeignKey('Songs', on_delete=models.CASCADE)
    last_time = models.DateTimeField()

    class Meta:
        unique_together = ('user_id', 'song_id')


class PlaylistSong(models.Model):
    list_id = models.ForeignKey('PlayLists', on_delete=models.CASCADE)
    song_id = models.ForeignKey('Songs', on_delete=models.CASCADE)
    add_date = models.DateTimeField()

    class Meta:
        unique_together = ('list_id', 'song_id')


class RankListSong(models.Model):
    list_id = models.ForeignKey('RankLists', on_delete=models.CASCADE)
    song_id = models.ForeignKey('Songs', on_delete=models.CASCADE)
    rank_index = models.PositiveIntegerField()

    class Meta:
        unique_together = ('list_id', 'song_id')


class UserLikePlaylist(models.Model):
    user_id = models.ForeignKey('Users', on_delete=models.CASCADE)
    list_id = models.ForeignKey('PlayLists', on_delete=models.CASCADE)

    class Meta:
        unique_together = ('list_id', 'user_id')


class ArtistInGroup(models.Model):
    group_id = models.ForeignKey('Artists', on_delete=models.CASCADE, related_name='group')
    artist_id = models.ForeignKey('Artists', on_delete=models.CASCADE, related_name='single')

