# File: admin.py
# Author: Saud Alotaibi
# Description: Registers game_review models with the Django admin site.

from django.contrib import admin
from .models import *

# Register all models so they are manageable through the Django admin panel
admin.site.register(Profile)
admin.site.register(Genre)
admin.site.register(VideoGame)
admin.site.register(GameLibraryEntry)
admin.site.register(Review)
