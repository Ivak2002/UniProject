from django.urls import path

from .views import CPUListView, GPUListView, MotherboardListView, RamListView, BuiltComputersListView, CPUUpdateView, \
    CPUDeleteView,GPUUpdateView,GPUDeleteView,RAMUpdateView,RAMDeleteView,ComputerUpdateView,ComputerDeleteView,MotherboardUpdateView, \
    MotherboardDeleteView

urlpatterns = [
    path('cpu/', CPUListView.as_view(), name='product-cpu'),
    path('gpu/', GPUListView.as_view(), name='product-gpu'),
    path('motherboard/', MotherboardListView.as_view(), name='product-motherboard'),
    path('ram/', RamListView.as_view(), name='product-ram'),
    path('built-computers/', BuiltComputersListView.as_view(), name='built-computers'),
    path('cpu/<int:pk>/edit/', CPUUpdateView.as_view(), name='cpu_edit'),
    path('cpu/<int:pk>/delete/', CPUDeleteView.as_view(), name='cpu_delete'),
    path('gpu/<int:pk>/edit/', GPUUpdateView.as_view(), name='gpu_edit'),
    path('gpu/<int:pk>/delete/', GPUDeleteView.as_view(), name='gpu_delete'),
    path('ram/<int:pk>/edit/', RAMUpdateView.as_view(), name='ram_edit'),
    path('ram/<int:pk>/delete/', RAMDeleteView.as_view(), name='ram_delete'),
    path('computer/<int:pk>/edit/', ComputerUpdateView.as_view(), name='computer_edit'),
    path('computer/<int:pk>/delete/', ComputerDeleteView.as_view(), name='computer_delete'),
    path('motherboard/<int:pk>/edit/', MotherboardUpdateView.as_view(), name='motherboard_edit'),
    path('motherboard/<int:pk>/delete/', MotherboardDeleteView.as_view(), name='motherboard_delete'),

]
