# File: views.py
# Author: Saud Alotaibi
# Description: Handles page logic, gets data from models, and sends it to templates.


from django.shortcuts import render
from django.urls import reverse
from .models import Profile, Post, Photo
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .forms import CreatePostForm, UpdateProfileForm, UpdatePostForm

# Create your views here.
class ProfileListView(ListView):
    '''Displays a list of all profiles.'''

    model = Profile
    template_name = 'mini_insta/show_all.html'
    context_object_name = 'profiles'

class ProfileDetailView(DetailView):
    '''Displays the detail page for one profile.'''

    model = Profile
    template_name = 'mini_insta/show_profile.html'
    context_object_name = 'profile'

class PostDetailView(DetailView):
    '''Displays the detail page for one post'''

    model = Post
    template_name = 'mini_insta/show_post.html'
    context_object_name = 'post'

class CreatePostView(CreateView):
    '''Handles the creation of a post. 
        1. Displays the HTML form to the user
        2. Proccess the form submission and stores the new Post object'''
    
    # Specifies the form and HTML template that is going to be shown to the user. 
    form_class = CreatePostForm
    template_name = 'mini_insta/create_post_form.html'

    def get_context_data(self):
        """Connects the post to the profile."""

        # Gets the context dictionary
        context = super().get_context_data()

        # Finds the profile using the primary key, stores it in the context dictionary
        pk = self.kwargs['pk']
        profile = Profile.objects.get(pk=pk)
        context['profile'] = profile

        return context
    
    def get_success_url(self):
        """Returns the page to redirect to after the form is submitted successfully."""

        # Redirects to the original profile
        pk = self.kwargs['pk']
        return reverse('show_profile', kwargs={'pk':pk})

    def form_valid(self, form):
        """Handles the form submission and saves the new object to the Django database."""


        # retrieve the PK from the URL pattern
        pk = self.kwargs['pk']
        profile = Profile.objects.get(pk=pk)
        form.instance.profile = profile  # attach this post to the profile

        # image_url = self.request.POST['image_url']

        # Photo.objects.create(post=self.object, image_url=image_url)


        # delegate the work to the superclass method form_valid:
        response = super().form_valid(form)

       
       
        # For each image file in the form submission, create a photo object with the image file
        # and connect it to the post.
        
        files = self.request.FILES.getlist('files') # get all the image files in the form submission
        for file in files:
            Photo.objects.create(post=self.object, image_file=file)

        return response
    

class UpdateProfileView(UpdateView):
    model = Profile
    form_class = UpdateProfileForm
    template_name = 'mini_insta/update_profile_form.html'


class DeletePostView(DeleteView):

    model = Post
    template_name = 'mini_insta/delete_post_form.html'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()

        pk = self.kwargs['pk']
        post = Post.objects.get(pk=pk)
        profile = post.profile

        context['post'] = post
        context['profile'] = profile

        return context
    
    def get_success_url(self):
        pk = self.kwargs['pk']
        post = Post.objects.get(pk=pk)

        profile = post.profile
        return reverse('show_profile', kwargs={'pk':profile.pk})
    
class UpdatePostView(UpdateView):
    model = Post
    form_class = UpdatePostForm
    template_name = 'mini_insta/update_post_form.html'
    context_object_name = 'post'

    def get_success_url(self):
        pk = self.kwargs['pk']
        return reverse('show_post', kwargs={'pk':pk})

class ShowFollowersDetailView(DetailView):
    model = Profile
    template_name = 'mini_insta/show_followers.html'
    context_object_name = 'profile'

class ShowFollowingDetailView(DetailView):
    model = Profile
    template_name = 'mini_insta/show_following.html'
    context_object_name = 'profile'

class ShowFeedView(DetailView):
    model = Profile
    template_name = 'mini_insta/show_feed.html'
    context_object_name = 'profile'

class SearchView(ListView):
    model = Profile
    template_name = 'mini_insta/search_results.html'
    context_object_name = 'profiles'

    def dispatch(self, request, *args, **kwargs):
        
        if 'query' not in self.request.GET:
            pk = self.kwargs['pk']
            profile = Profile.objects.get(pk=pk)
            context = {'profile': profile}

            return render(request, 'mini_insta/search.html', context)

        return super().dispatch(request, *args, **kwargs)

    def get_queryset(self):
        query = self.request.GET['query']
        posts = Post.objects.filter(caption__contains=query)
        return posts
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data()

        pk = self.kwargs['pk']
        profile = Profile.objects.get(pk=pk)

        query = ""
        if 'query' in self.request.GET:
            query = self.request.GET['query']
        
        profiles = Profile.objects.filter(username__contains=query) | Profile.objects.filter(display_name__contains=query) | Profile.objects.filter(bio_text__contains=query)

        context['profile'] = profile
        context['query'] = query
        context['profiles'] = profiles
        context['posts'] = self.get_queryset()

        return context
