from django.db import models

# Create your models here.
class Joke(models.Model):
    text = models.TextField(blank=True)
    contributor = models.TextField(blank=True)
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.contributor} said the following joke: {self.text}'


class Picture(models.Model):
    image_url = models.URLField(blank=True)
    contributor = models.TextField(blank=True)
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.contributor} uploaded the following image: {self.image_url}'