from django.contrib import admin
from .models import Brand, Car, Inquiry


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ['brand', 'name', 'year',
                    'price', 'fuel_type', 'is_available']
    list_filter = ['brand', 'fuel_type', 'transmission', 'is_available']
    search_fields = ['name', 'brand__name']
    list_editable = ['is_available']


@admin.register(Inquiry)
class InquiryAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone', 'email', 'car', 'status', 'created_at']
    list_filter = ['status']
    list_editable = ['status']
    search_fields = ['name', 'email']
