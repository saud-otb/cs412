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
        context = super().get_context_data(**kwargs)

        jokes = Joke.objects.all()
        pictures = Picture.objects.all()

        random_joke = random.choice(jokes)
        random_picture = random.choice(pictures)

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
    queryset = Joke.objects.all()
    serializer_class = JokeSerializer

class JokeDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Joke.objects.all()
    serializer_class = JokeSerializer

class PictureListAPIView(generics.ListCreateAPIView):
    queryset = Picture.objects.all()
    serializer_class = PictureSerializer

class PictureDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Picture.objects.all()
    serializer_class = PictureSerializer

class RandomJokeDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Joke.objects.all()
    serializer_class = JokeSerializer

    def get_object(self):
        jokes = list(Joke.objects.all())
        return random.choice(jokes)

class RandomPictureDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Picture.objects.all()
    serializer_class = PictureSerializer

    def get_object(self):
        pictures = list(Picture.objects.all())
        return random.choice(pictures)