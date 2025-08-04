from django.core.validators import MinLengthValidator
from django.db import models


class CPU(models.Model):
    name = models.CharField(max_length=50, validators=[MinLengthValidator(10)], unique=True)
    image = models.URLField()
    cores = models.PositiveIntegerField()
    threads = models.PositiveIntegerField()
    cache = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class GPU(models.Model):
    name = models.CharField(max_length=50, validators=[MinLengthValidator(10)], unique=True)
    image = models.URLField()
    bus = models.CharField(max_length=15, validators=[MinLengthValidator(5)])
    memory = models.CharField(max_length=15, validators=[MinLengthValidator(5)])
    memory_type = models.CharField(max_length=15, validators=[MinLengthValidator(5)])
    price = models.DecimalField(max_digits=8, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class MotherBoard(models.Model):
    name = models.CharField(max_length=50, validators=[MinLengthValidator(10)], unique=True)
    image = models.URLField()
    platform = models.CharField(max_length=15, validators=[MinLengthValidator(3)])
    socket = models.CharField(max_length=15, validators=[MinLengthValidator(5)])
    chipset = models.CharField(max_length=15, validators=[MinLengthValidator(5)])
    price = models.DecimalField(max_digits=8, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class RAM(models.Model):
    name = models.CharField(max_length=50, validators=[MinLengthValidator(10)], unique=True)
    image = models.URLField()
    type = models.CharField(max_length=15, validators=[MinLengthValidator(3)])
    frequency = models.CharField(max_length=15, validators=[MinLengthValidator(5)])
    size = models.CharField(max_length=15, validators=[MinLengthValidator(3)])
    price = models.DecimalField(max_digits=8, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.name


class BuiltComputers(models.Model):
    name = models.CharField(max_length=50, validators=[MinLengthValidator(10)], unique=True)
    image = models.URLField()
    ram = models.CharField(max_length=50, validators=[MinLengthValidator(10)])
    gpu = models.CharField(max_length=50, validators=[MinLengthValidator(10)])
    motherboard = models.CharField(max_length=50, validators=[MinLengthValidator(10)])
    cpu = models.CharField(max_length=50, validators=[MinLengthValidator(10)])
    storage = models.CharField(max_length=50, validators=[MinLengthValidator(10)])
    created_at = models.DateTimeField(auto_now_add=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return self.name
