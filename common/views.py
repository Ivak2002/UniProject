from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import HelpModel, OrderNoProfileModel, OrderProfileModel
from .forms import HelpForm, OrderNoProfileForm, OrderProfileForm
from django.views.generic import TemplateView
from django.shortcuts import redirect
from django.views import View
from django.shortcuts import render

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


class NoProfileOrderView(CreateView):
    model = OrderNoProfileModel
    form_class = OrderNoProfileForm
    template_name = 'order-no-profile.html'
    success_url = reverse_lazy('home')

    def get_initial(self):
        initial = super().get_initial()
        product = self.request.GET.get('name')
        price = self.request.GET.get('price')
        if product:
            initial['product'] = product
        if price:
            initial['price'] = price
        return initial

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('order-profile')
        return super().dispatch(request, *args, **kwargs)

class ProfileOrderView(CreateView):
    model = OrderProfileModel
    form_class = OrderProfileForm
    template_name = 'order-profile.html'
    success_url = reverse_lazy('home')

    def get_initial(self):
        initial = super().get_initial()
        product = self.request.GET.get('name')
        price = self.request.GET.get('price')
        initial['email'] = self.request.user.email
        initial['first_name'] = self.request.user.first_name
        initial['last_name'] = self.request.user.last_name
        if product:
            initial['product'] = product
        if price:
            initial['price'] = price
        return initial

    def form_valid(self, form):
        form.instance.logged_user= self.request.user
        form.instance.email = self.request.user.email
        form.instance.first_name = self.request.user.first_name
        form.instance.last_name = self.request.user.last_name
        return super().form_valid(form)


class CustomPermissionDeniedView(View):
    def get(self, request, exception=None):
        return render(request, '403.html', status=403)

class CustomPageNotFoundView(View):
    def get(self, request, exception=None):
        return render(request, '404.html', status=404)

def permission_denied_view(request, exception):
    return CustomPermissionDeniedView.as_view()(request, exception=exception)

def page_not_found_view(request, exception):
    return CustomPageNotFoundView.as_view()(request, exception=exception)