from django.shortcuts import render
from .models import Profile, Post
from django.views.generic import ListView, DetailView

# Create your views here.
class ProfileListView(ListView):

    model = Profile
    template_name = 'mini_insta/show_all.html'
    context_object_name = 'profiles'

class ProfileDetailView(DetailView):

    model = Profile
    template_name = 'mini_insta/show_profile.html'
    context_object_name = 'profile'

class PostDetailView(DetailView):

    model = Post
    template_name = 'mini_insta/show_post.html'
    context_object_name = 'post'
