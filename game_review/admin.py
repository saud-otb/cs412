from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Profile)
admin.site.register(Genre)
admin.site.register(VideoGame)
admin.site.register(GameLibraryEntry)
admin.site.register(Review)