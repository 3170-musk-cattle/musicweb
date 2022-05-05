from django.urls import path, include
from hydrogen import views


urlpatterns = [
    path('add_user/', views.add_user),
    path('show_users/', views.show_users),
    path('show_songs/', views.show_songs),
    path('add_song/', views.add_song),
    path('add_artist/', views.add_artist),
    path('show_artists/', views.show_artists),
    path('delete_artist/', views.delete_artist),
    path('add_from_file/', views.register_songs_from_file),
    path('show_songs/', views.show_songs)
]