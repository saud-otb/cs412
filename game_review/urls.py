from django.urls import path
from django.conf import settings
from .views import *

urlpatterns = [
    path('', ListGenreView.as_view(), name='home_page'),
    path('genre/<int:pk>/', DetailGenreGamesView.as_view(), name='show_genre_games'),
    path('game/<int:pk>/', DetailGameView.as_view(), name='show_video_game'),
    path('profile/<int:pk>/', DetailProfileView.as_view(), name='show_profile'),
    path('profiles/', ListProfileView.as_view(), name='show_all_profiles'),
    path('games/', ListGameView.as_view(), name='show_all_games'),
    path('profile/<int:pk>/want_to_play/', ListWantToPlayView.as_view(), name='want_to_play'),
    path('profile/<int:pk>/currently_playing', ListCurrentlyPlayingView.as_view(), name='currently_playing'),
    path('profile/<int:pk>/played', ListPlayedView.as_view(), name='played'),
]