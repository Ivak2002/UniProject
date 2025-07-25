from django.urls import path

from common.views import HomeView, HelpView, AboutView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('help/', HelpView.as_view(), name='help'),
    path('about-us/', AboutView.as_view(), name='about'),
]