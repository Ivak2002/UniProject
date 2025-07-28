from django.contrib import admin

from .models import CPU, GPU


@admin.register(CPU)
class CPUAdmin(admin.ModelAdmin):
    list_display = ('name', 'cores', 'threads', 'cache', 'price', 'image')
    list_editable = ('price', 'cores', 'threads', 'cache', 'image')
    search_fields = ('name','price', 'cores')

    fieldsets = (
        ('General', {
            'fields': ('name', 'image', 'price')
        }),
        ('Specs', {
            'fields': ('cores', 'threads', 'cache')
        }),
    )

@admin.register(GPU)
class GPUAdmin(admin.ModelAdmin):
    list_display = ('name', 'bus', 'price', 'image', 'memory_type', 'memory')
    list_editable = ('price', 'bus', 'memory_type', 'memory', 'image')
    search_fields = ('name','price', 'memory')

    fieldsets = (
        ('General', {
            'fields': ('name', 'image', 'price')
        }),
        ('Specs', {
            'fields': ('bus', 'memory', 'memory_type')
        }),
    )


