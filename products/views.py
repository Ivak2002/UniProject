from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, DeleteView, UpdateView, CreateView, TemplateView

from .forms import CPUForm, GPUForm, RAMForm, MotherboardForm, ComputerForm
from .mixins import SuperuserRequiredMixin, ReadOnlyMixin
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

class CPUUpdateView(LoginRequiredMixin, StaffRequiredMixin,ReadOnlyMixin, UpdateView):
    model = CPU
    fields = ['name', 'cores', 'threads', 'cache', 'image', 'price']
    template_name = 'cpu_edit.html'
    success_url = reverse_lazy('home')


class CPUDeleteView(LoginRequiredMixin, StaffRequiredMixin, DeleteView):
    model = CPU
    template_name = 'cpu_delete.html'
    success_url = reverse_lazy('home')
class GPUUpdateView(LoginRequiredMixin, StaffRequiredMixin,ReadOnlyMixin, UpdateView):
    model = GPU
    fields = ['name', 'bus', 'memory', 'memory_type', 'image', 'price']
    template_name = 'gpu_edit.html'
    success_url = reverse_lazy('home')

class GPUDeleteView(LoginRequiredMixin, StaffRequiredMixin, DeleteView):
    model = GPU
    template_name = 'gpu_delete.html'
    success_url = reverse_lazy('home')
class MotherboardUpdateView(LoginRequiredMixin, StaffRequiredMixin,ReadOnlyMixin, UpdateView):
    model = MotherBoard
    fields = ['name', 'platform', 'socket', 'chipset', 'image', 'price']
    template_name = 'motherboard_edit.html'
    success_url = reverse_lazy('home')

class MotherboardDeleteView(LoginRequiredMixin, StaffRequiredMixin, DeleteView):
    model = MotherBoard
    template_name = 'motherboard_delete.html'
    success_url = reverse_lazy('home')
class RAMUpdateView(LoginRequiredMixin, StaffRequiredMixin,ReadOnlyMixin, UpdateView):
    model = RAM
    fields = ['name', 'type', 'frequency', 'size', 'image', 'price']
    template_name = 'ram_edit.html'
    success_url = reverse_lazy('home')

class RAMDeleteView(LoginRequiredMixin, StaffRequiredMixin, DeleteView):
    model = RAM
    template_name = 'ram_delete.html'
    success_url = reverse_lazy('home')
class ComputerUpdateView(LoginRequiredMixin, StaffRequiredMixin, ReadOnlyMixin,UpdateView):
    model = BuiltComputers
    fields = ['name', 'ram', 'gpu', 'motherboard','cpu','storage', 'image', 'price']
    template_name = 'computer_edit.html'
    success_url = reverse_lazy('home')

class ComputerDeleteView(LoginRequiredMixin, StaffRequiredMixin, DeleteView):
    model = BuiltComputers
    template_name = 'computer_delete.html'
    success_url = reverse_lazy('home')

class AddProductView(LoginRequiredMixin, SuperuserRequiredMixin, TemplateView):
    template_name = 'add_product.html'

class AddCPUView(LoginRequiredMixin, SuperuserRequiredMixin, CreateView):
    model = CPU
    template_name = 'add_cpu.html'
    form_class = CPUForm
    success_url = reverse_lazy('home')

class AddGPUView(LoginRequiredMixin, SuperuserRequiredMixin, CreateView):
    model = GPU
    template_name = 'add_gpu.html'
    form_class = GPUForm
    success_url = reverse_lazy('home')

class AddRAMView(LoginRequiredMixin, SuperuserRequiredMixin, CreateView):
    model = RAM
    template_name = 'add_ram.html'
    form_class = RAMForm
    success_url = reverse_lazy('home')

class AddMotherBoardView(LoginRequiredMixin, SuperuserRequiredMixin, CreateView):
    model = MotherBoard
    template_name = 'add_motherboard.html'
    form_class = MotherboardForm
    success_url = reverse_lazy('home')

class AddComputerView(LoginRequiredMixin, SuperuserRequiredMixin, CreateView):
    model = BuiltComputers
    template_name = 'add_computer.html'
    form_class = ComputerForm
    success_url = reverse_lazy('home')