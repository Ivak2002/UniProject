from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    bio = models.TextField(blank=True)
    birth_date = models.DateField(null=True, blank=False)
    first_name = models.TextField(blank=False )
    last_name = models.TextField(blank=False)
