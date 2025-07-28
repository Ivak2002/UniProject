from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.forms import AuthenticationForm

from account.models import CustomUser


class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = CustomUser
        fields = ["username", "email", "password1", "password2", "bio", "birth_date", "first_name", "last_name"]

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

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            'bio',
            'birth_date',
        ]
