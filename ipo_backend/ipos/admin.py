from django.contrib import admin
from .models import IPO, IPODocument, IPONews


class IPODocumentInline(admin.TabularInline):
    model = IPODocument
    extra = 0
    readonly_fields = ['created_at']


class IPONewsInline(admin.TabularInline):
    model = IPONews
    extra = 0
    readonly_fields = ['created_at']


@admin.register(IPO)
class IPOAdmin(admin.ModelAdmin):
    list_display = [
        'company', 'issue_size', 'price_range', 'open_date', 
        'close_date', 'status', 'board', 'is_featured', 'is_recommended'
    ]
    list_filter = [
        'status', 'board', 'is_featured', 'is_recommended', 
        'open_date', 'close_date', 'company__sector'
    ]
    search_fields = ['company__name', 'registrar', 'lead_managers']
    ordering = ['-created_at']
    readonly_fields = [
        'created_at', 'updated_at', 'created_by', 'updated_by',
        'is_open', 'days_to_open', 'days_to_close', 'price_range'
    ]
    inlines = [IPODocumentInline, IPONewsInline]
    
    fieldsets = (
        ('Company & Basic Info', {
            'fields': ('company', 'issue_size', 'board', 'status')
        }),
        ('Pricing', {
            'fields': ('price_range_min', 'price_range_max', 'price_range', 'listing_price', 'lot_size')
        }),
        ('Important Dates', {
            'fields': ('open_date', 'close_date', 'listing_date', 'is_open', 'days_to_open', 'days_to_close')
        }),
        ('Subscription Details', {
            'fields': ('total_subscription', 'retail_subscription', 'qib_subscription', 'nii_subscription'),
            'classes': ('collapse',)
        }),
        ('Documents', {
            'fields': ('rhp_document', 'drhp_document'),
            'classes': ('collapse',)
        }),
        ('Additional Information', {
            'fields': ('registrar', 'lead_managers'),
            'classes': ('collapse',)
        }),
        ('Performance', {
            'fields': ('listing_gains', 'current_price'),
            'classes': ('collapse',)
        }),
        ('Flags', {
            'fields': ('is_featured', 'is_recommended')
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


@admin.register(IPODocument)
class IPODocumentAdmin(admin.ModelAdmin):
    list_display = ['ipo', 'document_type', 'title', 'created_at']
    list_filter = ['document_type', 'created_at']
    search_fields = ['ipo__company__name', 'title', 'description']
    ordering = ['-created_at']
    readonly_fields = ['created_at', 'uploaded_by']
    
    def save_model(self, request, obj, form, change):
        if not change:
            obj.uploaded_by = request.user
        super().save_model(request, obj, form, change)


@admin.register(IPONews)
class IPONewsAdmin(admin.ModelAdmin):
    list_display = ['ipo', 'title', 'source', 'created_at']
    list_filter = ['created_at', 'ipo__company__sector']
    search_fields = ['ipo__company__name', 'title', 'content']
    ordering = ['-created_at']
    readonly_fields = ['created_at', 'created_by']
    
    def save_model(self, request, obj, form, change):
        if not change:
            obj.created_by = request.user
        super().save_model(request, obj, form, change)
