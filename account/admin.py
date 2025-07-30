from django.contrib import admin

from account.models import CustomUser

@admin.register(CustomUser)
class CPUAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'bio', 'birth_date')
    search_fields = ('username','email', 'bio')

    fieldsets = (
        (None, {'fields': ('username', 'email', 'bio', 'birth_date', 'is_staff', 'is_superuser')}),
    )

