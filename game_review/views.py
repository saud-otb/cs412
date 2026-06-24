# File: views.py
# Author: Saud Alotaibi
# Description: Handles page logic, retrieves data from models, and sends it to templates.

from django.shortcuts import render, redirect
from django.urls import reverse
from django.conf import settings
from django.views.generic import *
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from .models import *
from .forms import *
from .ai import summarize_reviews


class MyLoginRequiredMixin(LoginRequiredMixin):
    '''Redirects unauthenticated users to the login page and exposes the
    logged in user's profile to subclasses and templates.'''

    def get_login_url(self):
        '''Returns the URL of the login page for this app.'''
        return reverse('login_final')

    def get_logged_in_user(self):
        '''Returns the Profile linked to the currently authenticated user.'''
        return Profile.objects.filter(user=self.request.user).first()

    def get_context_data(self, **kwargs):
        '''Adds the logged-in user's profile to the template context.'''
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            context['logged_in_user'] = self.get_logged_in_user()
        return context

class ListGenreView(ListView):
    '''Displays the home page with all genres as clickable cards.'''
    model = Genre
    template_name = 'game_review/show_genres.html'
    context_object_name = 'genres'

class DetailGenreGamesView(DetailView):
    '''Displays all games belonging to a single genre.'''
    model = Genre
    template_name = 'game_review/show_genre_games.html'
    context_object_name = 'genre'

    def get_context_data(self, **kwargs):
        '''Adds the list of games for this genre to the template context.'''
        context = super().get_context_data(**kwargs)

        pk = self.kwargs['pk']
        games = VideoGame.objects.filter(genre=pk)

        context['games'] = games

        return context

class DetailGameView(DetailView):
    '''Displays a game's details, reviews, and AI-generated overview.'''
    model = VideoGame
    template_name = 'game_review/show_video_game.html'
    context_object_name = 'game'

    def get_context_data(self, **kwargs):
        '''Adds reviews, AI summary, and library status to the template context.'''
        context = super().get_context_data(**kwargs)

        pk = self.kwargs['pk']

        # Fetch all reviews for this game via the library entry relationship
        reviews = Review.objects.filter(game_library_entry__video_game=pk)
        context['reviews'] = reviews

        game = self.object
        review_count = reviews.count()

        # Regenerate the AI summary only when the review count has changed
        if settings.GEMINI_API_KEY and review_count > 0 and game.ai_summary_review_count != review_count:
            try:
                game.ai_summary = summarize_reviews(game, reviews)
                game.ai_summary_review_count = review_count
                game.save()
            except Exception:
                pass

        context['ai_summary'] = game.ai_summary

        # Check if the logged-in user has already added this game to their library
        if self.request.user.is_authenticated:
            profile = Profile.objects.filter(user=self.request.user).first()
            context['logged_in_user'] = profile
            if profile:
                context['in_library'] = GameLibraryEntry.objects.filter(profile=profile, video_game=game).exists()

        return context

class ListProfileView(ListView):
    '''Lists all user profiles.'''
    model = Profile
    template_name = 'game_review/show_all_profiles.html'
    context_object_name = 'profiles'

class DetailProfileView(DetailView):
    '''Displays a single user profile and links to their game library.'''
    model = Profile
    template_name = 'game_review/show_profile.html'
    context_object_name = 'profile'

    def get_context_data(self, **kwargs):
        '''Adds the logged-in user's profile to the template context.'''
        context = super().get_context_data(**kwargs)

        if self.request.user.is_authenticated:
            context['logged_in_user'] = Profile.objects.filter(user=self.request.user).first()

        return context

class ListGameView(ListView):
    '''Lists all video games in the database.'''
    model = VideoGame
    template_name = 'game_review/show_all_games.html'
    context_object_name = 'games'

class ListWantToPlayView(ListView):
    '''Lists all games a profile has marked as Want to Play.'''
    model = GameLibraryEntry
    template_name = 'game_review/game_library/show_want_to_play.html'
    context_object_name = 'entries'

    def get_queryset(self):
        '''Returns Want to Play entries for the profile specified in the URL.'''
        return GameLibraryEntry.objects.filter(profile__pk=self.kwargs['pk'], status="Want to Play")

class ListCurrentlyPlayingView(ListView):
    '''Lists all games a profile is currently playing.'''
    model = GameLibraryEntry
    template_name = 'game_review/game_library/show_currently_playing.html'
    context_object_name = 'entries'

    def get_queryset(self):
        '''Returns Currently Playing entries for the profile specified in the URL.'''
        return GameLibraryEntry.objects.filter(profile__pk=self.kwargs['pk'], status="Currently Playing")

class ListPlayedView(ListView):
    '''Lists all games a profile has finished playing.'''
    model = GameLibraryEntry
    template_name = 'game_review/game_library/show_played.html'
    context_object_name = 'entries'

    def get_queryset(self):
        '''Returns Played entries for the profile specified in the URL.'''
        return GameLibraryEntry.objects.filter(profile__pk=self.kwargs['pk'], status="Played")

class CreateReviewView(MyLoginRequiredMixin, CreateView):
    '''Displays a form to write a review for a played game.'''
    model = Review
    form_class = CreateReviewForm
    template_name = 'game_review/create_review.html'

    def get_context_data(self, **kwargs):
        '''Passes the library entry to the template, or sets not_valid if the game hasn't been played.'''
        context = super().get_context_data(**kwargs)

        pk = self.kwargs['pk']
        entry = GameLibraryEntry.objects.get(pk=pk)

        # Only allow reviews for entries with Played status
        if entry.status != "Played":
            context['not_valid'] = True
        else:
            context['entry'] = entry

        return context

    def form_valid(self, form):
        '''Links the new review to the library entry before saving.'''
        pk = self.kwargs['pk']
        entry = GameLibraryEntry.objects.get(pk=pk)

        form.instance.game_library_entry = entry

        return super().form_valid(form)

    def get_success_url(self):
        '''Redirects to the game's detail page after the review is submitted.'''
        pk = self.kwargs['pk']
        entry = GameLibraryEntry.objects.get(pk=pk)
        return reverse('show_video_game_final', kwargs={'pk': entry.video_game.pk})

class UpdateReviewView(MyLoginRequiredMixin, UpdateView):
    '''Displays a form to edit an existing review.'''
    model = Review
    form_class = UpdateReviewForm
    template_name = 'game_review/update_review_form.html'
    context_object_name = 'review'

    def get_success_url(self):
        '''Redirects to the game's detail page after the review is updated.'''
        review = self.get_object()
        return reverse('show_video_game_final', kwargs={'pk': review.game_library_entry.video_game.pk})

class UpdateGameLibraryEntryView(MyLoginRequiredMixin, UpdateView):
    '''Displays a form to change a library entry's category.'''
    model = GameLibraryEntry
    form_class = UpdateGameLibraryEntryForm
    template_name = 'game_review/update_library_entry_form.html'
    context_object_name = 'entry'

    def get_success_url(self):
        '''Redirects to the profile page after the category change is saved.'''
        entry = self.get_object()
        return reverse('show_profile_final', kwargs={'pk': entry.profile.pk})

class AddToLibraryView(MyLoginRequiredMixin, CreateView):
    '''Displays a form to add a game to the logged-in user's library.'''
    model = GameLibraryEntry
    form_class = AddToLibraryForm
    template_name = 'game_review/add_to_library_form.html'

    def get_context_data(self, **kwargs):
        '''Passes the game object to the template.'''
        context = super().get_context_data(**kwargs)
        context['game'] = VideoGame.objects.get(pk=self.kwargs['pk'])
        return context

    def form_valid(self, form):
        '''Sets the profile, game, and initial hours before saving the entry.'''
        form.instance.profile = self.get_logged_in_user()
        form.instance.video_game = VideoGame.objects.get(pk=self.kwargs['pk'])
        # New entries always start at zero hours
        form.instance.hours_played = 0
        return super().form_valid(form)

    def get_success_url(self):
        '''Redirects to the game's detail page after the entry is added.'''
        return reverse('show_video_game_final', kwargs={'pk': self.kwargs['pk']})

class UpdateHoursPlayedView(MyLoginRequiredMixin, UpdateView):
    '''Displays a form to update hours played for a currently-playing game.'''
    model = GameLibraryEntry
    form_class = UpdateHoursPlayedForm
    template_name = 'game_review/update_hours_form.html'
    context_object_name = 'entry'

    def get_success_url(self):
        '''Redirects to the Currently Playing page for this profile.'''
        entry = self.get_object()
        return reverse('currently_playing_final', kwargs={'pk': entry.profile.pk})

class DeleteReviewView(MyLoginRequiredMixin, DeleteView):
    '''Displays a confirmation page before permanently deleting a review.'''
    model = Review
    template_name = 'game_review/delete_review_form.html'
    context_object_name = 'review'

    def get_success_url(self):
        '''Redirects to the game's detail page after the review is deleted.'''
        review = self.get_object()
        return reverse('show_video_game_final', kwargs={'pk': review.game_library_entry.video_game.pk})

def logout_page(request):
    '''Renders the logout confirmation page to the user.'''
    template_name = 'game_review/logout.html'
    return render(request, template_name)

class CreateProfileView(CreateView):
    '''Displays a form to the user to create their user account and profile.'''
    form_class = CreateProfileForm
    template_name = 'game_review/create_profile_form.html'

    def get_context_data(self, **kwargs):
        '''Passes the UserCreationForm to the template, pre-filled if re-submitting.'''
        context = super().get_context_data(**kwargs)
        if self.request.POST:
            context['user_form'] = UserCreationForm(self.request.POST)
        else:
            context['user_form'] = UserCreationForm()
        return context

    def form_valid(self, form):
        '''Creates the Django user account and logs them in, then saves the profile.'''
        # Validate the user account form separately from the profile form
        user_form = UserCreationForm(self.request.POST)

        if not user_form.is_valid():
            return self.form_invalid(form)

        user = user_form.save()

        # Log the new user in automatically so they land on their profile
        login(self.request, user, backend='django.contrib.auth.backends.ModelBackend')

        form.instance.user = user

        return super().form_valid(form)

    def get_success_url(self):
        '''Redirects to the user's new profile after registration.'''
        return reverse('my_profile_final')

class SearchView(ListView):
    '''Displays a search form and shows matching games, genres, and profiles.'''
    model = VideoGame
    template_name = 'game_review/search_results.html'
    context_object_name = 'games'

    def dispatch(self, request, *args, **kwargs):
        '''Shows the empty search page if no query was provided.'''
        if 'query' not in self.request.GET:
            return render(request, 'game_review/search.html')
        return super().dispatch(request, *args, **kwargs)

    def get_queryset(self):
        '''Returns games matching the search query by title or description.'''
        query = self.request.GET.get('query', '')
        return VideoGame.objects.filter(title__icontains=query) | VideoGame.objects.filter(description__icontains=query)

    def get_context_data(self, **kwargs):
        '''Adds matching genres, profiles, and the query string to the template context.'''
        context = super().get_context_data(**kwargs)

        query = self.request.GET.get('query', '')
        context['query'] = query

        # Search genres and profiles using the same query string
        context['genres'] = Genre.objects.filter(name__icontains=query) | Genre.objects.filter(description__icontains=query)
        context['profiles'] = Profile.objects.filter(display_name__icontains=query) | Profile.objects.filter(bio__icontains=query)

        if self.request.user.is_authenticated:
            context['logged_in_user'] = Profile.objects.filter(user=self.request.user).first()

        return context

def my_profile(request):
    '''Redirects the logged in user to their own profile page.'''
    if not request.user.is_authenticated:
        return redirect('login_final')

    profile = Profile.objects.filter(user=request.user).first()
    if profile:
        return redirect('show_profile_final', pk=profile.pk)

    return redirect('create_profile_final')
