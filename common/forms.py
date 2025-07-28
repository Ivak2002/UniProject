from django import forms
from .models import HelpModel

class HelpForm(forms.ModelForm):
    class Meta:
        model = HelpModel
        fields = ['question_theme', 'email', 'question']

        widgets = {
            'question_theme': forms.TextInput(attrs={'placeholder': 'GPU Problem'}),
            'question': forms.Textarea(attrs={'placeholder': 'So my GPU started overheating....'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].widget.attrs['readonly'] = True