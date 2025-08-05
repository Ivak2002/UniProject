from django.contrib import admin

from .models import HelpModel, OrderNoProfileModel, OrderProfileModel


@admin.register(HelpModel)
class HelpAdmin(admin.ModelAdmin):
    list_display = ('question_theme', 'email', 'question', 'created_at', 'current_sender')
    search_fields = ('email',)


@admin.register(OrderNoProfileModel)
class OrderNoProfileAdmin(admin.ModelAdmin):
    list_display = ('product', 'telephone_number', 'price', 'created_at')
    search_fields = ('telephone_number',)


@admin.register(OrderProfileModel)
class OrderProfileAdmin(admin.ModelAdmin):
    list_display = ('product', 'telephone_number', 'email', 'first_name', 'last_name', 'delivery_choices', 'address', 'logged_user', 'price', 'created_at')
    search_fields = ('telephone_number','email', 'delivery_choices')
    fieldsets = (
        ('Data', {
            'fields': ('product', 'telephone_number', 'email', 'first_name', 'last_name'),
        }),
        ('Information', {
            'fields': ('delivery_choices', 'address', 'logged_user', 'price', 'created_at'),
        }),
    )