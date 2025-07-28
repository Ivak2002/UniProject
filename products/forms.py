from django import forms
from .models import CPU

class CPUForm(forms.ModelForm):
    class Meta:
        model = CPU
        fields = ['name', 'image', 'cores', 'threads', 'base_clock', 'boost_clock', 'l3_cache', 'price']
