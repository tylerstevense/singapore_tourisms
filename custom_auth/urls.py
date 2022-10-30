from django.urls import include, path
from custom_auth.forms import RegistrationForm
from . import views

urlpatterns = [
    path('profile/', views.profile, name="profile"),    
    path('edit_profile/', views.edit_profile, name="edit_profile"),    
    path('profiles/', views.profiles, name='profiles'),
    path('profile/<int:pk>/', views.ProfileDetailView.as_view(), name='profile_detail'),
]