from django.urls import path
from django.conf import settings
from .views import ProfileListView, ProfileDetailView

urlpatterns = [
    path(r'', ProfileListView.as_view(), name='show_all_profiles'),
    path(r'<int:pk>/', ProfileDetailView.as_view(), name='show_profile'),
    
]