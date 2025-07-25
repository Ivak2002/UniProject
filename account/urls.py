from django.urls import path
from .views import RegisterView, UserLoginView, CustomLogoutView, SettingsView

urlpatterns = [
   path('register/', RegisterView.as_view(), name='register'),
   path('login/', UserLoginView.as_view(), name='login'),
   path('logout/', CustomLogoutView.as_view(), name='logout'),

   path('settings/', SettingsView.as_view(), name='settings'),
]