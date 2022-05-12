from django.urls import path, include
from oxygen import views


urlpatterns = [
    path('test/', views.view_something),
    path('insert/', views.insert_db)
]
