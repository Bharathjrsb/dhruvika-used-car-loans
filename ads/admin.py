from django.contrib import admin
from .models import Ad

@admin.register(Ad)
class AdAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_active', 'created_at')
    list_filter = ('is_active', 'created_at')
    search_fields = ('title',)
