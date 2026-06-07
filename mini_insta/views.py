# File: views.py
# Author: Saud Alotaibi
# Description: Handles page logic, gets data from models, and sends it to templates.


from django.shortcuts import render
from django.urls import reverse
from .models import Profile, Post, Photo, Follower, Likes
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .forms import CreatePostForm, UpdateProfileForm, UpdatePostForm, CreateProfileForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
# Create your views here.
class MyLoginRequiredMixin(LoginRequiredMixin):

    def get_login_url(self):
        return reverse('login')
    
    def get_logged_in_user(self):
        return Profile.objects.get(user=self.request.user)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['logged_in_user'] = self.get_logged_in_user()
        return context
    
class ProfileListView(ListView, MyLoginRequiredMixin):
    '''Displays a list of all profiles.'''

    model = Profile
    template_name = 'mini_insta/show_all.html'
    context_object_name = 'profiles'

    def get_context_data(self):
        context = super().get_context_data()

        if self.request.user.is_authenticated:
            context["logged_in_user"] = self.get_logged_in_user()

        return context

class ProfileDetailView(DetailView, MyLoginRequiredMixin):
    '''Displays the detail page for one profile.'''

    model = Profile
    template_name = 'mini_insta/show_profile.html'
    context_object_name = 'profile'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        if self.request.user.is_authenticated:
            logged_in_user = self.get_logged_in_user()
            context['logged_in_user'] = logged_in_user

            follows = Follower.objects.filter(profile=self.object, follower_profile=logged_in_user)

            if len(follows) == 0:
                context["is_following"] = False
            else:
                context["is_following"] = True

        return context

class PostDetailView(DetailView, MyLoginRequiredMixin):
    '''Displays the detail page for one post'''

    model = Post
    template_name = 'mini_insta/show_post.html'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        if self.request.user.is_authenticated:
            logged_in_user = self.get_logged_in_user()
            context['logged_in_user'] = logged_in_user

            likes = Likes.objects.filter(profile=logged_in_user, post=self.object)

            if len(likes) == 0:
                context["has_liked"] = False
            else:
                context["has_liked"] = True

        return context

class CreatePostView(MyLoginRequiredMixin, CreateView):
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
        profile = self.get_logged_in_user()
        context['profile'] = profile

        return context
    
    def get_success_url(self):
        """Returns the page to redirect to after the form is submitted successfully."""

        # Redirects to the original profile
        pk = self.get_logged_in_user().pk
        return reverse('show_profile', kwargs={'pk':pk})

    def form_valid(self, form):
        """Handles the form submission and saves the new object to the Django database."""


        # retrieve the PK from the URL pattern
        profile = self.get_logged_in_user()
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
    

class UpdateProfileView(MyLoginRequiredMixin, UpdateView):
    '''Displays the HTML form to the user to update their profile and handles the form submission'''
    model = Profile
    form_class = UpdateProfileForm
    template_name = 'mini_insta/update_profile_form.html'

    def get_object(self):
        return self.get_logged_in_user()
    


class DeletePostView(MyLoginRequiredMixin, DeleteView):
    '''Displays the HTML form to the user to delete their post and handles the form submission'''
    model = Post
    template_name = 'mini_insta/delete_post_form.html'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        '''Includes the profile of the post and the post itself in the context dictionary'''
        context = super().get_context_data()

        pk = self.kwargs['pk']
        post = Post.objects.get(pk=pk)
        profile = post.profile

        context['post'] = post
        context['profile'] = profile

        return context
    
    def get_success_url(self):
        '''Returns a url after the user successfully deletes their post'''
        pk = self.kwargs['pk']
        post = Post.objects.get(pk=pk)

        # Redirect the user to their profile page after deleting the post
        profile = post.profile
        return reverse('show_profile', kwargs={'pk':profile.pk})
    
    
class UpdatePostView(MyLoginRequiredMixin, UpdateView):
    '''Displays the HTML form to the user to update their post and handles the form submission'''
    model = Post
    form_class = UpdatePostForm
    template_name = 'mini_insta/update_post_form.html'
    context_object_name = 'post'

    def get_success_url(self):
        '''Returns a url after the user successfully deletes their post'''

        # Redirects the user to their post after successfully updating it
        pk = self.kwargs['pk']
        return reverse('show_post', kwargs={'pk':pk})

class ShowFollowersDetailView(DetailView):
    '''Displays the page to show the user all profiles that are following them'''
    model = Profile
    template_name = 'mini_insta/show_followers.html'
    context_object_name = 'profile'

class ShowFollowingDetailView(DetailView):
    '''Displays the page to show the user all the profiles that they are following'''
    model = Profile
    template_name = 'mini_insta/show_following.html'
    context_object_name = 'profile'

class ShowFeedView(MyLoginRequiredMixin, DetailView):
    '''Displays a list of posts from all the profiles that the user is following'''
    model = Profile
    template_name = 'mini_insta/show_feed.html'
    context_object_name = 'profile'

    def get_object(self):
        return self.get_logged_in_user()
    
class SearchView(MyLoginRequiredMixin, ListView):
    '''Displays an HTML form for the user to search profiles and posts, and handles the form submission'''
    model = Profile
    template_name = 'mini_insta/search_results.html'
    context_object_name = 'profiles'

    def dispatch(self, request, *args, **kwargs):
        
        if 'query' not in self.request.GET:
            profile = self.get_logged_in_user()
            context = {'profile': profile}

            return render(request, 'mini_insta/search.html', context)

        return super().dispatch(request, *args, **kwargs)

    def get_queryset(self):
        query = self.request.GET['query']
        posts = Post.objects.filter(caption__contains=query)
        return posts
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data()


        profile = self.get_logged_in_user()

        query = ""
        if 'query' in self.request.GET:
            query = self.request.GET['query']
        
        profiles = Profile.objects.filter(username__contains=query) | Profile.objects.filter(display_name__contains=query) | Profile.objects.filter(bio_text__contains=query)

        context['profile'] = profile
        context['query'] = query
        context['profiles'] = profiles
        context['posts'] = self.get_queryset()

        return context

def logout_page(request):
    '''Renders the logout confirmation page to the user'''
    template_name = 'mini_insta/logout.html'
    return render(request, template_name)

class CreateProfileView(CreateView):
    '''Displays a form to the user to create their user account and profile.'''
    form_class = CreateProfileForm
    template_name = 'mini_insta/create_profile_form.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user_form'] = UserCreationForm

        return context

    def form_valid(self, form):
        user_form = UserCreationForm(self.request.POST)

        user = user_form.save()

        login(self.request, user, backend='django.contrib.auth.backends.ModelBackend')

        form.instance.user = user

        return super().form_valid(form)
    

class FollowProfileView(ProfileDetailView):
    """Allows the logged in profile to follow another profile."""

    def dispatch(self, request, *args, **kwargs):

        if not request.user.is_authenticated:
            return super().dispatch(request, *args, **kwargs)

        profile = Profile.objects.get(pk=self.kwargs["pk"])
        logged_in_user = self.get_logged_in_user()

        Follower.objects.create(profile=profile, follower_profile=logged_in_user)

        return super().dispatch(request, *args, **kwargs)


class DeleteFollowView(ProfileDetailView):
    """Allows the logged in profile to unfollow another profile."""

    def dispatch(self, request, *args, **kwargs):

        if not request.user.is_authenticated:
            return super().dispatch(request, *args, **kwargs)

        profile = Profile.objects.get(pk=self.kwargs["pk"])
        logged_in_user = self.get_logged_in_user()
        
        follow = Follower.objects.get(profile=profile, follower_profile=logged_in_user)

        follow.delete()

        return super().dispatch(request, *args, **kwargs)


class LikePostView(PostDetailView):
    """Allows the logged in profile to like a post."""

    def dispatch(self, request, *args, **kwargs):

        if not request.user.is_authenticated:
            return super().dispatch(request, *args, **kwargs)

        post = Post.objects.get(pk=self.kwargs["pk"])
        logged_in_user = self.get_logged_in_user()

        Likes.objects.create(profile=logged_in_user, post=post)

        return super().dispatch(request, *args, **kwargs)


class DeleteLikeView(PostDetailView):
    """Removes the logged in profile's like from a post."""

    def dispatch(self, request, *args, **kwargs):

        if not request.user.is_authenticated:
            return super().dispatch(request, *args, **kwargs)

        post = Post.objects.get(pk=self.kwargs["pk"])
        logged_in_user = self.get_logged_in_user()

        like = Likes.objects.get(profile=logged_in_user, post=post)

        like.delete()

        return super().dispatch(request, *args, **kwargs)