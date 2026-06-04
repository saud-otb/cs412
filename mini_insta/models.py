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
    

    def get_followers(self):
        followers = Follower.objects.filter(profile=self)

        followers_profile = []
        for follower in followers:
            followers_profile.append(follower.follower_profile)

        return followers_profile
    
    def get_num_followers(self):
        followers_profile = self.get_followers()
        return len(followers_profile)

    def get_following(self):
        following = Follower.objects.filter(follower_profile=self)

        following_profile = []
        for follow in following:
            following_profile.append(follow.profile)

        return following_profile
    
    def get_num_following(self):
        following_profiles = self.get_following()
        return len(following_profiles)
    
    def get_post_feed(self):
        following_profiles = self.get_following()
        post_feed = Post.objects.filter(profile__in=following_profiles).order_by("-timestamp")
        return post_feed

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
    
    def get_first_photo(self):
        all_photos = self.get_all_photos()
        if all_photos == None or len(all_photos) == 0:
            return
        return all_photos[0]
        
    def get_all_comments(self):
        comments = Comment.objects.filter(post=self)
        return comments
    
    def get_likes(self):
        likes = Likes.objects.filter(post=self)
        len = 0
        for like in likes:
            len += 1
        return len

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
        photo = self.post.get_first_photo()
        if photo.image_url:
            return photo.image_url
        else:
            return photo.image_file.url

    def __str__(self):
        '''Return the string repersentation of this photo object'''
        return f'{self.post.profile.username} posted a photo from this url: {self.get_image_url()}'
    

class Follower(models.Model):
    profile = models.ForeignKey("Profile", on_delete=models.CASCADE, related_name="profile")
    follower_profile = models.ForeignKey("Profile", on_delete=models.CASCADE, related_name="follower_profile")
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        '''Return the string repersentation of this follower object'''
        return f'{self.follower_profile} follows {self.profile}'
    
   
class Comment(models.Model):
    post = models.ForeignKey("Post", on_delete=models.CASCADE)
    profile = models.ForeignKey("Profile", on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now=True)
    text = models.TextField(blank=True)

    def __str__(self):
        return f'{self.profile.username} wrote the following comment: {self.text}'
    

class Likes(models.Model):
    post = models.ForeignKey("Post", on_delete=models.CASCADE)
    profile = models.ForeignKey("Profile", on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.profile.username} liked the post made by {self.post.profile.username}'