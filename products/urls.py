from django.urls import path

from .views import CPUListView, GPUListView

urlpatterns = [
    path('cpu/', CPUListView.as_view(), name='product-cpu'),
    path('gpu/', GPUListView.as_view(), name='product-gpu'),

]