from django.contrib import admin
from.models import Product
# Register your models here.

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')
    search_fields = ('name', 'description')
    list_filter = ('name',)  # You can add more fields for filtering as needed
