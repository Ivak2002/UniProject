from django.contrib.auth.views import LoginView
from django.urls import path

from common.views import HomeView, HelpView, AboutView, NoProfileOrderView, ProfileOrderView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('help/', HelpView.as_view(), name='help'),
    path('about-us/', AboutView.as_view(), name='about'),
    path('order-no-profile/', NoProfileOrderView.as_view(), name='order-no-profile'),
path('order-profile/', ProfileOrderView.as_view(), name='order-profile')
]
