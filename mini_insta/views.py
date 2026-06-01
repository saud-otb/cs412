from django.shortcuts import render
from django.urls import reverse
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

    def get_context_data(self):
        context = super().get_context_data()

        pk = self.kwargs['pk']
        profile = Profile.objects.get(pk=pk)
        context['profile'] = profile

        return context
    
    def get_success_url(self):
        pk = self.kwargs['pk']
        return reverse('show_profile', kwargs={'pk':pk})

    def form_valid(self, form):
        pk = self.kwargs['pk']
        profile = Profile.objects.get(pk=pk)
        form.instance.profile = profile

        # image_url = self.request.POST['image_url']

        # Photo.objects.create(post=self.object, image_url=image_url)

        files = self.request.FILES.getlist('files')

        for file in files:
            Photo.objects.create(post=self.object, image_file=file)

        return super().form_valid(form)

