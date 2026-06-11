from rest_framework import serializers
from .models import *
 

class JokeSerializer(serializers.ModelSerializer):
    '''A serializer for the Article model. Specify which model/fields to send in the API.'''
    class Meta:
        model = Joke
        fields = ['text', 'contributor', 'timestamp']


class PictureSerializer(serializers.ModelSerializer):
    '''A serializer for the Picture model.'''
    class Meta:
        model = Picture
        fields = ['image_url', 'contributor', 'timestamp']