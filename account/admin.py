from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
from .forms import RegisterForm, CustomUserChangeForm  # assuming you have them

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    add_form = RegisterForm
    form = CustomUserChangeForm
    model = CustomUser

    list_display = ('username', 'email', 'is_staff', 'is_superuser')
    search_fields = ('username', 'email')

    fieldsets = (
        (None, {'fields': ('username', 'email', 'password')}),
        ('Personal Info', {'fields': ('bio', 'birth_date')}),
        ('Permissions', {'fields': ('is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2', 'bio', 'birth_date', 'is_staff', 'is_superuser'),
        }),
    )