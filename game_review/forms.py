# File: forms.py
# Author: Saud Alotaibi
# Description: Defines forms used to collect and validate user input.

from django import forms
from .models import *


class CreateReviewForm(forms.ModelForm):
    '''A form for a user to submit a new review for a game they have played.'''

    class Meta:
        '''Associates this form with the Review model.'''
        model = Review
        fields = ['rating', 'review_title', 'review_text', 'recommended']

class UpdateReviewForm(forms.ModelForm):
    '''A form for a user to edit an existing review.'''

    class Meta:
        '''Associates this form with the Review model.'''
        model = Review
        fields = ['rating', 'review_title', 'review_text', 'recommended']

class UpdateGameLibraryEntryForm(forms.ModelForm):
    '''A form for a user to change a library entry's play status.'''

    class Meta:
        '''Associates this form with the GameLibraryEntry model.'''
        model = GameLibraryEntry
        fields = ['status']

class AddToLibraryForm(forms.ModelForm):
    '''A form for a user to add a game to their library with an initial status.'''

    class Meta:
        '''Associates this form with the GameLibraryEntry model.'''
        model = GameLibraryEntry
        fields = ['status']

class UpdateHoursPlayedForm(forms.ModelForm):
    '''A form for a user to update the hours played for a currently-playing game.'''

    class Meta:
        '''Associates this form with the GameLibraryEntry model.'''
        model = GameLibraryEntry
        fields = ['hours_played']

class CreateProfileForm(forms.ModelForm):
    '''A form to create a new user profile in the database.'''

    class Meta:
        '''Associates this form with the Profile model.'''
        model = Profile
        fields = ['display_name', 'bio', 'profile_image']
