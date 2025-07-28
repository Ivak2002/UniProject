from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.views.generic import  DetailView, UpdateView, DeleteView
from django.views.generic.edit import FormView
from django.contrib.auth import login
from .forms import RegisterForm, CustomLoginForm, CustomUserChangeForm
from .models import CustomUser


class RegisterView(FormView):
    template_name = 'register.html'
    form_class = RegisterForm

    def get_success_url(self):
        return reverse_lazy('home')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return super().form_valid(form)



class UserLoginView(LoginView):
    template_name = 'login.html'
    authentication_form = CustomLoginForm

    def get_success_url(self):
        return reverse_lazy('home')

class CustomLogoutView(LogoutView):
    http_method_names = ['post']
    next_page = 'home'


class ProfileView(LoginRequiredMixin, DetailView):
    model = CustomUser
    template_name = 'profile.html'
    context_object_name = 'user_profile'

    def get_object(self, queryset=None):
        return self.request.user

class EditProfileView(UpdateView):
    model = CustomUser
    form_class = CustomUserChangeForm
    template_name = 'edit-profile.html'
    context_object_name = 'user_profile'
    success_url = reverse_lazy('profile')
    def get_object(self, queryset=None):
        return self.request.user

class DeleteProfileView(DeleteView):
    model = CustomUser
    template_name = 'delete-profile.html'
    context_object_name = 'user_profile'
    success_url = reverse_lazy('profile')

    def get_object(self, queryset=None):
        return self.request.user