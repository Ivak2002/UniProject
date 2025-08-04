from django import forms
from .models import CPU, GPU, MotherBoard, RAM, BuiltComputers


class CPUForm(forms.ModelForm):
    class Meta:
        model = CPU
        fields = ['name', 'image', 'cores', 'threads', 'cache', 'price']


class GPUForm(forms.ModelForm):
    class Meta:
        model = GPU
        fields = ['name', 'image', 'bus', 'memory', 'memory_type', 'price']


class MotherboardForm(forms.ModelForm):
    class Meta:
        model = MotherBoard
        fields = ['name', 'image', 'platform', 'socket', 'chipset', 'price']


class RAMForm(forms.ModelForm):
    class Meta:
        model = RAM
        fields = ['name', 'image', 'type', 'frequency', 'size', 'price']


class ComputerForm(forms.ModelForm):
    class Meta:
        model = BuiltComputers
        fields = ['name', 'image', 'ram', 'gpu', 'motherboard', 'cpu', 'storage', 'price']
