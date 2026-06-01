from django.shortcuts import render
from .models import Profile, Post, Photo
from django.views.generic import ListView, DetailView, CreateView
from .forms import CreatePostForm

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

class CreatePostView(CreateView):
    form_class = CreatePostForm
    template_name = 'mini_insta/create_post_form.html'

    def get_context_data(self, **kwargs):
        context_dictionary = super().get_context_data(**kwargs)

        pk = self.kwargs['pk']
        profile = Profile.objects.get(pk=pk)
        context_dictionary['profile'] = profile

        return context_dictionary

    def form_valid(self, form):
        pk = self.kwargs['pk']
        profile = Profile.objects.get(pk=pk)
        form.instance.profile = profile

        image_url = self.request.POST['image_url']

        Photo.objects.create(post=self.object, image_url=image_url)
        
        return super.form_valid(form)

