from django.contrib import admin

from .models import CPU, GPU, RAM, MotherBoard, BuiltComputers


@admin.register(CPU)
class CPUAdmin(admin.ModelAdmin):
    list_display = ('name', 'image', 'threads', 'cache', 'price', 'cores')
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
    list_display = ('name', 'image', 'price', 'memory', 'memory_type', 'bus')
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

@admin.register(RAM)
class RAMAdmin(admin.ModelAdmin):
    list_display = ('name', 'image', 'type', 'megahertz', 'frequency', 'price')
    list_editable = ('price', 'type', 'megahertz', 'frequency', 'image')
    search_fields = ('name','price', 'type')

    fieldsets = (
        ('General', {
            'fields': ('name', 'image', 'price')
        }),
        ('Specs', {
            'fields': ('frequency', 'megahertz', 'type')
        }),
    )

@admin.register(MotherBoard)
class MotherBoardAdmin(admin.ModelAdmin):
    list_display = ('name', 'image', 'platform', 'socket', 'chipset', 'price')
    list_editable = ('price', 'platform', 'socket', 'chipset', 'image')
    search_fields = ('name','price', 'socket')

    fieldsets = (
        ('General', {
            'fields': ('name', 'image', 'price')
        }),
        ('Specs', {
            'fields': ('platform', 'socket', 'chipset')
        }),
    )

@admin.register(BuiltComputers)
class BuiltComputersAdmin(admin.ModelAdmin):
    list_display = ('name', 'image', 'ram', 'gpu', 'motherboard', 'cpu', 'box', 'storage', 'price')
    list_editable = ('name', 'image', 'ram', 'gpu', 'motherboard', 'cpu', 'box', 'storage', 'price')
    search_fields = ('name','price', 'ram', 'gpu', 'motherboard', 'cpu', 'storage', 'ram')

    fieldsets = (
        ('General', {
            'fields': ('name', 'image', 'price')
        }),
        ('Specs', {
            'fields': ('ram', 'gpu', 'motherboard', 'cpu', 'box', 'storage')
        }),
    )



