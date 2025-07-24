
from django.views.generic import TemplateView

class HomeView(TemplateView):
    template_name = 'home.html'

class HelpView(TemplateView):
    template_name = 'help.html'

class AboutView(TemplateView):
    template_name = 'about-us.html'