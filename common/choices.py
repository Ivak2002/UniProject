from django.db import models

class DeliveryChoices(models.TextChoices):
    ECONT = 'ECONT', 'ECONT'
    SPEEDY = 'SPEEDY', 'SPEEDY'