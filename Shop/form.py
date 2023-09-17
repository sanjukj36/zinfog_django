from django import forms
from .models import Product
from Customer.models import Order


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description','rating', 'price']

class OrderForm(forms.ModelForm):
    class Meta:
        model =Order
        fields = ['Status']
