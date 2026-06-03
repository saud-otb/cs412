# File: views.py
# Author: Saud Alotaibi
# Description: Registers models so they can be viewed and managed in the Django admin site.

from django.contrib import admin

# Register your models here.
from .models import Profile, Post, Photo, Follower
admin.site.register(Profile)
admin.site.register(Post)
admin.site.register(Photo)
admin.site.register(Follower)