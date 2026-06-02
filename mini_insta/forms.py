# File: views.py
# Author: Saud Alotaibi
# Description: Defines forms used to collect and validate user input.

from django import forms
from .models import *

class CreatePostForm(forms.ModelForm):
    '''A form to add a post to our database'''

    class Meta:
        '''Associate this form with the Post model from our database'''
        model = Post
        fields = ['caption']

class UpdateProfileForm(forms.ModelForm):
    '''A form to update our profile in the database'''

    class Meta:
        '''Associate this form with the Profile model from our database'''
        model = Profile
        fields = ['display_name', 'profile_image_url', 'bio_text']