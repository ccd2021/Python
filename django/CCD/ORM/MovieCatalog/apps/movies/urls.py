from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('register_user', views.register_user, name='user'),
    path('home', views.home),
    path('register_movie', views.register_movie),
    path('movie/<int:movie_id>', views.movie, name='movie'),
    path('movies', views.movies, name='movies'),
    path('director', views.director, name='director'),
    path('director_movies/<int:director_id>', views.director_movies),
]
