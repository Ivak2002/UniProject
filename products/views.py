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
class GPUUpdateView(LoginRequiredMixin, StaffRequiredMixin, UpdateView):
    model = GPU
    fields = ['name', 'bus', 'memory', 'memory_type', 'image', 'price']
    template_name = 'gpu_edit.html'
    success_url = reverse_lazy('home')

class GPUDeleteView(LoginRequiredMixin, StaffRequiredMixin, DeleteView):
    model = GPU
    template_name = 'gpu_delete.html'
    success_url = reverse_lazy('home')
class MotherboardUpdateView(LoginRequiredMixin, StaffRequiredMixin, UpdateView):
    model = MotherBoard
    fields = ['name', 'platform', 'socket', 'chipset', 'image', 'price']
    template_name = 'motherboard_edit.html'
    success_url = reverse_lazy('home')

class MotherboardDeleteView(LoginRequiredMixin, StaffRequiredMixin, DeleteView):
    model = MotherBoard
    template_name = 'motherboard_delete.html'
    success_url = reverse_lazy('home')
class RAMUpdateView(LoginRequiredMixin, StaffRequiredMixin, UpdateView):
    model = RAM
    fields = ['name', 'type', 'frequency', 'size', 'image', 'price']
    template_name = 'ram_edit.html'
    success_url = reverse_lazy('home')

class RAMDeleteView(LoginRequiredMixin, StaffRequiredMixin, DeleteView):
    model = RAM
    template_name = 'ram_delete.html'
    success_url = reverse_lazy('home')
class ComputerUpdateView(LoginRequiredMixin, StaffRequiredMixin, UpdateView):
    model = BuiltComputers
    fields = ['name', 'ram', 'gpu', 'motherboard','cpu','storage', 'image', 'price']
    template_name = 'computer_edit.html'
    success_url = reverse_lazy('home')

class ComputerDeleteView(LoginRequiredMixin, StaffRequiredMixin, DeleteView):
    model = BuiltComputers
    template_name = 'computer_delete.html'
    success_url = reverse_lazy('home')