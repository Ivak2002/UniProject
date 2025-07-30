from django.urls import path

from .models import MotherBoard
from .views import CPUListView, GPUListView, MotherboardListView, RamListView, BuiltComputersListView

urlpatterns = [
    path('cpu/', CPUListView.as_view(), name='product-cpu'),
    path('gpu/', GPUListView.as_view(), name='product-gpu'),
    path('motherboard/', MotherboardListView.as_view(), name='product-motherboard'),
    path('ram/', RamListView.as_view(), name='product-ram'),
    path('built-computers/', BuiltComputersListView.as_view(), name='built-computers'),
]
