from django import forms
from .models import HelpModel, OrderNoProfileModel, OrderProfileModel


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

class OrderNoProfileForm(forms.ModelForm):
    class Meta:
        model = OrderNoProfileModel
        fields = ['product', 'telephone_number', 'price']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['product'].widget.attrs['readonly'] = True
        self.fields['price'].widget.attrs['readonly'] = True

class OrderProfileForm(forms.ModelForm):
    class Meta:
        model = OrderProfileModel
        fields = ['product', 'telephone_number','email','first_name','last_name','delivery_choices','address', 'price']


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['product'].widget.attrs['readonly'] = True
        self.fields['price'].widget.attrs['readonly'] = True
        self.fields['first_name'].widget.attrs['readonly'] = True
        self.fields['last_name'].widget.attrs['readonly'] = True