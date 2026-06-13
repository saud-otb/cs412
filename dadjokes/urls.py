
# File: urls.py
# Author: Saud Alotaibi
# Description: Defines the URL patterns for the Dad Jokes application,
# including HTML pages and REST API endpoints for Jokes and Pictures.


from django.urls import path
from django.conf import settings
from .views import *

urlpatterns = [
    path(r'', RandomJokeView.as_view(), name='first_page'),
    path(r'random', RandomJokeView.as_view(), name='random_joke'),
    path(r'jokes', JokeListView.as_view(), name='all_jokes'),
    path(r'joke/<int:pk>', DetailJokeView.as_view(), name='joke'),
    path(r'pictures', ListPictureView.as_view(), name='all_pictures'),
    path(r'picture/<int:pk>', DetailPictureView.as_view(), name='picture'),
    path(r'api/', RandomJokeDetailAPIView.as_view()),
    path(r'api/random', RandomJokeDetailAPIView.as_view()),
    path(r'api/jokes', JokeListAPIView.as_view()),
    path(r'api/joke/<int:pk>', JokeDetailAPIView.as_view()),
    path(r'api/pictures', PictureListAPIView.as_view()),
    path(r'api/picture/<int:pk>', PictureDetailAPIView.as_view()),
    path(r'api/random_picture', RandomPictureDetailAPIView.as_view()),
]