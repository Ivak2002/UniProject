from django.contrib.auth.models import AbstractUser
from django.db import models
from django import forms

class CustomUser(AbstractUser):
    bio = models.TextField(blank=True)
    birth_date = models.DateField(null = True, blank = False)
