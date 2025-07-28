
from django.db import models

class CPU(models.Model):
    name = models.CharField(max_length=100)
    image = models.URLField()
    cores = models.PositiveIntegerField()
    threads = models.PositiveIntegerField()
    cache = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class GPU(models.Model):
    name = models.CharField(max_length=100)
    image = models.URLField()
    bus = models.CharField(max_length=100)
    memory = models.CharField(max_length=100)
    memory_type = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
