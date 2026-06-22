
from django import forms
from .models import *


class CreateReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['rating', 'review_title', 'review_text', 'recommended']

class UpdateReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['rating', 'review_title', 'review_text', 'recommended']