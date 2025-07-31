from django.urls import path

from .views import CPUListView, GPUListView, MotherboardListView, RamListView, BuiltComputersListView, CPUUpdateView, \
    CPUDeleteView

urlpatterns = [
    path('cpu/', CPUListView.as_view(), name='product-cpu'),
    path('gpu/', GPUListView.as_view(), name='product-gpu'),
    path('motherboard/', MotherboardListView.as_view(), name='product-motherboard'),
    path('ram/', RamListView.as_view(), name='product-ram'),
    path('built-computers/', BuiltComputersListView.as_view(), name='built-computers'),
    path('cpu/<int:pk>/edit/', CPUUpdateView.as_view(), name='cpu_edit'),
    path('cpu/<int:pk>/delete/', CPUDeleteView.as_view(), name='cpu_delete'),

]
