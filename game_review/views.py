from django.shortcuts import render
from django.urls import reverse
from django.views.generic import *
from .models import *
from .forms import *

# Create your views here.
class ListGenreView(ListView):
    model = Genre
    template_name = 'game_review/show_genres.html'
    context_object_name = 'genres'

class DetailGenreGamesView(DetailView):
    model = Genre
    template_name = 'game_review/show_genre_games.html'
    context_object_name = 'genre'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        pk = self.kwargs['pk']
        games = VideoGame.objects.filter(genre=pk)

        context['games'] = games

        return context

class DetailGameView(DetailView):
    model = VideoGame
    template_name = 'game_review/show_video_game.html'
    context_object_name = 'game'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        pk = self.kwargs['pk']
        reviews = Review.objects.filter(game_library_entry__video_game = pk)

        context['reviews'] = reviews
        return context
    
class ListProfileView(ListView):
    model = Profile
    template_name = 'game_review/show_all_profiles.html'
    context_object_name = 'profiles'

class DetailProfileView(DetailView):
    model = Profile
    template_name = 'game_review/show_profile.html'
    context_object_name = 'profile'

class ListGameView(ListView):
    model = VideoGame
    template_name = 'game_review/show_all_games.html'
    context_object_name = 'games'

class ListWantToPlayView(ListView):
    model = GameLibraryEntry
    template_name = 'game_review/game_library/show_want_to_play.html'
    context_object_name = 'entries'

    def get_queryset(self):
        pk = self.kwargs['pk']
        want_to_play = GameLibraryEntry.objects.filter(profile__pk=pk) & GameLibraryEntry.objects.filter(status="Want to Play")
        return want_to_play

class ListCurrentlyPlayingView(ListView):
    model = GameLibraryEntry
    template_name = 'game_review/game_library/show_currently_playing.html'
    context_object_name = 'entries'

    def get_queryset(self):
        pk = self.kwargs['pk']
        currently_playing = GameLibraryEntry.objects.filter(profile__pk=pk, status="Currently Playing")
        return currently_playing
    
class ListPlayedView(ListView):
    model = GameLibraryEntry
    template_name = 'game_review/game_library/show_played.html'
    context_object_name = 'entries'

    def get_queryset(self):
        pk = self.kwargs['pk']
        played = GameLibraryEntry.objects.filter(profile__pk=pk, status="Played")
        return played

class CreateReviewView(CreateView):
    model = Review
    form_class = CreateReviewForm
    template_name = 'game_review/create_review.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        pk = self.kwargs['pk']
        entry = GameLibraryEntry.objects.get(pk=pk)

        if entry.status != "Played":
            context['not_valid'] = True
        else:
            context['entry'] = entry 
        
        return context
    
    def form_valid(self, form):
        pk = self.kwargs['pk']
        entry = GameLibraryEntry.objects.get(pk=pk)

        form.instance.game_library_entry = entry

        return super().form_valid(form)
    
    def get_success_url(self):
        pk = self.kwargs['pk']
        return reverse('show_video_game', kwargs={'pk': pk})

class UpdateReviewView(CreateView):
    model = Review
    form_class = UpdateReviewForm
    template_name = 'game_review/update_review_form.html'
    

    

