from django.urls import path
from .views import RegisterView, UserLoginView, CustomLogoutView, ProfileView, EditProfileView, \
   DeleteProfileView

urlpatterns = [
   path('register/', RegisterView.as_view(), name='register'),
   path('login/', UserLoginView.as_view(), name='login'),
   path('logout/', CustomLogoutView.as_view(), name='logout'),
   path('settings/', ProfileView.as_view(), name='profile'),
   path('settings/edit/', EditProfileView.as_view(), name='edit-profile'),
   path('settings/delete/', DeleteProfileView.as_view(), name='delete-profile'),
]