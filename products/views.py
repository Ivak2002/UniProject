from django.views.generic import ListView
from .models import CPU, GPU


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
