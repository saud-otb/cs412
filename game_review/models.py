# File: models.py
# Author: Saud Alotaibi
# Description: Defines the database structure for profiles, games, library entries, and reviews.

from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


class Profile(models.Model):
    '''Represents a Gamer's Hub user profile with basic personal information.'''

    # related_name avoids clashing with other apps that also link to User 9mini-insta)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='game_review_profile')
    display_name = models.TextField()
    bio = models.TextField(blank=True)
    profile_image = models.ImageField(blank=True)
    date_created = models.DateTimeField(auto_now=True)  # auto-set to now on every save

    def get_absolute_url(self):
        '''Returns the URL for this profile's detail page.'''
        return reverse('show_profile_final', kwargs={'pk': self.pk})

    def __str__(self):
        return self.display_name


class Genre(models.Model):
    '''Represents a video game genre used to categorize games.'''

    name = models.TextField()
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class VideoGame(models.Model):
    '''Stores information about a video game title.'''

    title = models.TextField()
    developer = models.TextField()
    publisher = models.TextField()

    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)

    release_date = models.DateField()
    description = models.TextField()
    cover_image = models.ImageField(blank=True)
    steam_app_id = models.IntegerField(blank=True, null=True)  # optional Steam store link

    # Cached AI summary and the review count at the time it was generated
    ai_summary = models.TextField(blank=True)
    ai_summary_review_count = models.IntegerField(default=0)

    def __str__(self):
        return self.title


class GameLibraryEntry(models.Model):
    '''Connects a user profile to a game, tracking play status and hours.'''

    # Valid options for the status field shown in forms and the admin
    STATUS_CHOICES = [
        ('Want to Play', 'Want to Play'),
        ('Currently Playing', 'Currently Playing'),
        ('Played', 'Played'),
    ]

    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    video_game = models.ForeignKey(VideoGame, on_delete=models.CASCADE)
    status = models.TextField(choices=STATUS_CHOICES)
    date_added = models.DateTimeField(auto_now=True)  # auto-updated on every save
    hours_played = models.IntegerField()

    def __str__(self):
        return (f"{self.profile} - {self.video_game} - {self.status}")


class Review(models.Model):
    '''Stores a review written by a user for a game they have played.'''

    # A review belongs to a library entry (profile + game pair)
    game_library_entry = models.ForeignKey(GameLibraryEntry, on_delete=models.CASCADE)

    rating = models.IntegerField()
    review_title = models.TextField()
    review_text = models.TextField()
    recommended = models.BooleanField()
    date_submitted = models.DateTimeField(auto_now=True)  # auto-set on every save

    def __str__(self):
        return (f"{self.game_library_entry.profile}'s review of {self.game_library_entry}")
