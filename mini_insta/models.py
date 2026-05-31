from django.db import models

# Create your models here.
class Profile(models.Model):
    username = models.TextField(blank=True)
    display_name = models.TextField(blank=True)
    profile_image_url = models.URLField(blank=True)
    bio_text = models.TextField(blank=True)
    join_date = models.DateTimeField(auto_now=True)

    def get_all_posts(self):
        all_posts = Post.objects.filter(profile=self).order_by('timestamp')
        return all_posts

    def __str__(self):
        return f'{self.username}'
    
    
class Post(models.Model):

    profile = models.ForeignKey("Profile", on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now=True)
    caption = models.TextField(blank=True)

    def get_all_photos(self):
        all_photos = Photo.objects.filter(post=self).order_by('timestamp')
        return all_photos

    def __str__(self):
        return f'{self.profile.username} made a post with the following caption: {self.caption}'
    
class Photo(models.Model):

    post = models.ForeignKey("Post", on_delete=models.CASCADE)
    image_url = models.URLField(blank=True)
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.post.profile.username} posted a photo from this url: {self.image_url}'