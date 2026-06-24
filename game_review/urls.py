# File: urls.py
# Author: Saud Alotaibi
# Description: Defines the app-level URL routes and connects each path to its matching view.

from django.urls import path
from django.conf import settings
from django.contrib.auth import views as auth_views
from .views import *

urlpatterns = [
    # Genre routes
    path('', ListGenreView.as_view(), name='home_page_final'),
    path('genre/<int:pk>/', DetailGenreGamesView.as_view(), name='show_genre_games_final'),

    # Game routes
    path('game/<int:pk>/', DetailGameView.as_view(), name='show_video_game_final'),
    path('game/<int:pk>/add_to_library', AddToLibraryView.as_view(), name='add_to_library_final'),

    # Profile routes
    path('profile/<int:pk>/', DetailProfileView.as_view(), name='show_profile_final'),
    path('profiles/', ListProfileView.as_view(), name='show_all_profiles_final'),
    path('games/', ListGameView.as_view(), name='show_all_games_final'),

    # Library routes (keyed by the profile's pk so any visitor can view any library)
    path('profile/<int:pk>/want_to_play/', ListWantToPlayView.as_view(), name='want_to_play_final'),
    path('profile/<int:pk>/currently_playing', ListCurrentlyPlayingView.as_view(), name='currently_playing_final'),
    path('profile/<int:pk>/played', ListPlayedView.as_view(), name='played_final'),

    # Review routes
    path('entry/<int:pk>/review/create', CreateReviewView.as_view(), name='create_review_final'),
    path('review/<int:pk>/update', UpdateReviewView.as_view(), name='update_review_final'),
    path('review/<int:pk>/delete', DeleteReviewView.as_view(), name='delete_review_final'),

    # Library entry management routes
    path('entry/<int:pk>/update_status', UpdateGameLibraryEntryView.as_view(), name='update_library_entry_final'),
    path('entry/<int:pk>/update_hours', UpdateHoursPlayedView.as_view(), name='update_hours_final'),

    # Authentication routes
    path('login/', auth_views.LoginView.as_view(template_name='game_review/login.html'), name='login_final'),
    path('logout_page/', logout_page, name='logout_page_final'),
    path('logout/', auth_views.LogoutView.as_view(next_page='home_page_final'), name='logout_final'),
    path('create_profile/', CreateProfileView.as_view(), name='create_profile_final'),

    # Search and user routes
    path('search/', SearchView.as_view(), name='search_final'),
    path('my_profile/', my_profile, name='my_profile_final'),
]
