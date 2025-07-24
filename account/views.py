from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views.generic.edit import FormView
from django.contrib.auth import login
from .forms import RegisterForm,CustomLoginForm

class RegisterView(FormView):
    template_name = 'register.html'
    form_class = RegisterForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return super().form_valid(form)



class UserLoginView(LoginView):
    template_name = 'login.html'
    authentication_form = CustomLoginForm

class UserLoginView(LoginView):
    template_name = 'login.html'
    authentication_form = CustomLoginForm