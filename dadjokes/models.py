# File: models.py 
# Author: Saud Alotaibi
# Description: Defines the Joke and Picture models used to store dad jokes, 
# picture URLs, contributors, and timestamps in the database. """

from django.db import models

# Create your models here.
class Joke(models.Model):
    '''Represents one dad joke submitted by a contributor.'''
    text = models.TextField(blank=True)
    contributor = models.TextField(blank=True)
    timestamp = models.DateTimeField(auto_now=True)

    '''Returns the string repersentation of a Joke Object'''
    def __str__(self):
        return f'{self.contributor} said the following joke: {self.text}'


class Picture(models.Model):
    '''Represents one picture submitted by a contributor.'''
    image_url = models.URLField(blank=True)
    contributor = models.TextField(blank=True)
    timestamp = models.DateTimeField(auto_now=True)

    '''Returns the string repersentation of a Picture object'''
    def __str__(self):
        return f'{self.contributor} uploaded the following image: {self.image_url}'