# File: views.py 
# Author: Saud Alotaibi
# Description: Defines the views and REST API endpoints used to display, 
# retrieve, create, update, and delete Joke and Picture objects. """



from django.shortcuts import render
from django.urls import reverse
from .models import Joke, Picture
from django.views.generic import ListView, DetailView, TemplateView
from rest_framework import generics
from .serializers import *
import random
# Create your views here.

class JokeListView(ListView):
    '''Shows a page with all Jokes (no images)'''
    model = Joke
    template_name = 'dadjokes/all_jokes.html'
    context_object_name = 'jokes'


class RandomJokeView(TemplateView):
    '''Show one Joke and one Picture selected at random'''

    template_name = 'dadjokes/random_joke.html'

    def get_context_data(self, **kwargs):
        '''Adds a random Joke and Picture to the template context.'''
        context = super().get_context_data(**kwargs)

        # Retrieves all Joke and Picture objects.
        jokes = Joke.objects.all()
        pictures = Picture.objects.all()

        # Selects one random Joke and Picture.
        random_joke = random.choice(jokes)
        random_picture = random.choice(pictures)

        # Makes the selected objects available in the template.
        context['joke'] = random_joke
        context['picture'] = random_picture

        return context
    
class DetailJokeView(DetailView):
    '''Shows one Joke.'''
    model = Joke
    template_name = 'dadjokes/joke.html'
    context_object_name = 'joke'

class DetailPictureView(DetailView):
    '''Shows one Picture'''
    model = Picture
    template_name = 'dadjokes/picture.html'
    context_object_name = 'picture'

class ListPictureView(ListView):
    '''Shows all Pictures'''
    model = Picture
    template_name = 'dadjokes/all_pictures.html'
    context_object_name = 'pictures'


class JokeListAPIView(generics.ListCreateAPIView):
    '''Provides an API endpoint for listing and creating Jokes.'''
    queryset = Joke.objects.all()
    serializer_class = JokeSerializer

class JokeDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    '''Provides an API endpoint for retrieving, updating, or deleting one Joke.'''
    queryset = Joke.objects.all()
    serializer_class = JokeSerializer

class PictureListAPIView(generics.ListCreateAPIView):
    '''Provides an API endpoint for listing and creating Pictures.'''
    queryset = Picture.objects.all()
    serializer_class = PictureSerializer

class PictureDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    '''Provides an API endpoint for retrieving, updating, or deleting one Picture.'''
    queryset = Picture.objects.all()
    serializer_class = PictureSerializer

class RandomJokeDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    '''Provides an API endpoint that returns one randomly selected Joke.'''
    queryset = Joke.objects.all()
    serializer_class = JokeSerializer

    def get_object(self):
        '''Returns one randomly selected Joke object.'''
        # Converts the QuerySet into a list
        jokes = list(Joke.objects.all())
        return random.choice(jokes)

class RandomPictureDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    '''Provides an API endpoint that returns one randomly selected Picture.'''
    queryset = Picture.objects.all()
    serializer_class = PictureSerializer

    def get_object(self):
        '''Returns one randomly selected Picture object.'''
        # Converts the QuerySet into a list
        pictures = list(Picture.objects.all())
        return random.choice(pictures)