from django.contrib import admin

# Register your models here.
from django.contrib import admin
from.models import Order
# Register your models here.

@admin.register(Order)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')

    list_filter = ('name',)  # You can add more fields for filtering as needed
