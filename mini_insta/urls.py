# File: views.py
# Author: Saud Alotaibi
# Description: Defines the app-level URL routes and connects each path to its matching view.

from django.urls import path
from django.conf import settings
# from .views import ProfileListView, ProfileDetailView, PostDetailView, CreatePostView, UpdateProfileView, DeletePostView, UpdatePostView
from .views import *
urlpatterns = [
    path(r'', ProfileListView.as_view(), name='show_all_profiles'),
    path(r'<int:pk>/', ProfileDetailView.as_view(), name='show_profile'),
    path(r'post/<int:pk>/', PostDetailView.as_view(), name='show_post'),
    path(r'profile/<int:pk>/create_post', CreatePostView.as_view(), name='create_post'),
    path(r'profile/<int:pk>/update', UpdateProfileView.as_view(), name='update_profile'),
    path(r'post/<int:pk>/delete', DeletePostView.as_view(), name='delete_post'),
    path(r'post/<int:pk>/update', UpdatePostView.as_view(), name='update_post'),
    path(r'profile/<int:pk>/followers', ShowFollowersDetailView.as_view(), name='show_followers'),
    path(r'profile/<int:pk>/following', ShowFollowingDetailView.as_view(), name='show_following'),
]