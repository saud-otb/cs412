# File: views.py
# Author: Saud Alotaibi
# Description: Defines the database structure for profiles, posts, and photos.

from django.db import models
from django.urls import reverse

# Create your models here.
class Profile(models.Model):
    '''Represents a Mini Insta user profile with basic user information.'''
    username = models.TextField(blank=True)
    display_name = models.TextField(blank=True)
    profile_image_url = models.URLField(blank=True)
    bio_text = models.TextField(blank=True)
    join_date = models.DateTimeField(auto_now=True)

    def get_all_posts(self):
        '''Returns all posts created by this profile.'''
        all_posts = Post.objects.filter(profile=self).order_by('timestamp')
        return all_posts

    def get_absolute_url(self):
        return reverse('show_profile', kwargs={'pk':self.pk})

    def __str__(self):
        '''Return a string reprsentation of this profile object'''
        return f'{self.username}'
    
    
class Post(models.Model):
    '''Represents a post created by a profile, including its caption and timestamp.'''
    profile = models.ForeignKey("Profile", on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now=True)
    caption = models.TextField(blank=True)

    def get_all_photos(self):
        '''Returns all photos connected to this post.'''
        all_photos = Photo.objects.filter(post=self).order_by('timestamp')
        return all_photos

    def __str__(self):
        '''Return a string representation of this post object'''
        return f'{self.profile.username} made a post with the following caption: {self.caption}'
    
class Photo(models.Model):
    '''Represents an image connected to a post, allowing one post to have many photos.'''
    post = models.ForeignKey("Post", on_delete=models.CASCADE)
    image_url = models.URLField(blank=True)
    image_file = models.ImageField(blank=True)
    timestamp = models.DateTimeField(auto_now=True)

    def get_image_url(self):
        '''Returns the url of this image'''

        # If image_url is null, it returns the image file's url
        if self.image_url:
            return self.image_url
        else:
            return self.image_file.url

    def __str__(self):
        '''Return the string repersentation of this photo object'''
        return f'{self.post.profile.username} posted a photo from this url: {self.get_image_url()}'