from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm
User = get_user_model()

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2", "bio", "birth_date"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            label= field.label or field_name.replace("_", " ")
            field.widget.attrs.update({
                'class': 'form-input',
                'placeholder': f'Enter your {label.lower()}',
            })
        self.fields['birth_date'].widget.attrs.update({
            'placeholder': '2000-02-20',
        })
        self.fields['email'].widget.attrs.update({
            'placeholder': 'example@gmail.com',
        })



class CustomLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)  # Only call once!

        for field_name, field in self.fields.items():
            field.widget.attrs.update({
                'class': 'form-input',
                'placeholder': f'Enter your {field.label.lower()}'
            })

