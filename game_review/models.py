from django.db import models

# Create your models here.

class Profile(models.Model):
    """Store information about one user profile."""

    display_name = models.TextField()
    bio = models.TextField(blank=True)
    profile_image = models.ImageField(blank=True)
    date_created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.display_name


class Genre(models.Model):
    """Represent a video game genre."""

    name = models.TextField()
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class VideoGame(models.Model):
    """Store information about a video game."""

    title = models.TextField()
    developer = models.TextField()
    publisher = models.TextField()

    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)

    release_date = models.DateField()
    description = models.TextField()
    cover_image = models.ImageField(blank=True)
    steam_app_id = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.title


class GameLibraryEntry(models.Model):
    """Connect a profile to a game in the user's library."""

    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)

    video_game = models.ForeignKey(VideoGame, on_delete=models.CASCADE)

    status = models.TextField()

    date_added = models.DateTimeField(auto_now=True)
    hours_played = models.IntegerField()

    def __str__(self):
        return (f"{self.profile} - {self.video_game} - {self.status}")


class Review(models.Model):
    """Store a review written for a played game."""

    game_library_entry = models.ForeignKey(GameLibraryEntry, on_delete=models.CASCADE)

    rating = models.IntegerField()
    review_title = models.TextField()
    review_text = models.TextField()
    recommended = models.BooleanField()
    date_submitted = models.DateTimeField(auto_now=True)

    def __str__(self):
        return (f"{self.game_library_entry.profile}'s review of {self.game_library_entry}")