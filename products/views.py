from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, DeleteView, UpdateView
from .models import CPU, GPU, MotherBoard, RAM, BuiltComputers


class CPUListView(ListView):
    model = CPU
    template_name = 'product-cpu.html'
    context_object_name = 'cpus'
    paginate_by = 6

class GPUListView(ListView):
    model = GPU
    template_name = 'product-gpu.html'
    context_object_name = 'gpus'
    paginate_by = 6

class MotherboardListView(ListView):
    model = MotherBoard
    template_name = 'product-motherboard.html'
    context_object_name = 'motherboards'
    paginate_by = 6

class RamListView(ListView):
    model = RAM
    template_name = 'product-ram.html'
    context_object_name = 'rams'
    paginate_by = 6

class BuiltComputersListView(ListView):
    model = BuiltComputers
    template_name = 'built-computers.html'
    context_object_name = 'built_computers'
    paginate_by = 6

class StaffRequiredMixin(UserPassesTestMixin):

    def test_func(self):
        return self.request.user.is_staff

class CPUUpdateView(LoginRequiredMixin, StaffRequiredMixin, UpdateView):
    model = CPU
    fields = ['name', 'cores', 'threads', 'cache', 'image', 'price']
    template_name = 'cpu_edit.html'
    success_url = reverse_lazy('home')

class CPUDeleteView(LoginRequiredMixin, StaffRequiredMixin, DeleteView):
    model = CPU
    template_name = 'cpu_delete.html'
    success_url = reverse_lazy('home')