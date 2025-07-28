from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import HelpModel
from .forms import HelpForm
from django.views.generic import TemplateView

class HomeView(TemplateView):
    template_name = 'home.html'

class AboutView(TemplateView):
    template_name = 'about-us.html'

class HelpView(LoginRequiredMixin, CreateView):
    model = HelpModel
    form_class = HelpForm
    template_name = 'help.html'
    success_url = reverse_lazy('home')

    def get_initial(self):
        initial = super().get_initial()
        initial['email'] = self.request.user.email
        return initial

    def form_valid(self, form):
        form.instance.current_sender = self.request.user
        form.instance.email = self.request.user.email
        return super().form_valid(form)