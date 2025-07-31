from django.contrib import admin
from .models import Company


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ['name', 'sector', 'industry', 'established_year', 'total_ipos', 'created_at']
    list_filter = ['sector', 'industry', 'created_at']
    search_fields = ['name', 'description', 'sector', 'industry']
    ordering = ['name']
    readonly_fields = ['created_at', 'updated_at', 'created_by', 'updated_by', 'total_ipos', 'upcoming_ipos']
    
    fieldsets = (
        ('Basic Information', {
            'fields': ('name', 'description', 'logo')
        }),
        ('Company Details', {
            'fields': ('sector', 'industry', 'website', 'established_year', 'headquarters')
        }),
        ('Statistics', {
            'fields': ('total_ipos', 'upcoming_ipos'),
            'classes': ('collapse',)
        }),
        ('Metadata', {
            'fields': ('created_at', 'updated_at', 'created_by', 'updated_by'),
            'classes': ('collapse',)
        })
    )
    
    def save_model(self, request, obj, form, change):
        if not change:
            obj.created_by = request.user
        else:
            obj.updated_by = request.user
        super().save_model(request, obj, form, change)
