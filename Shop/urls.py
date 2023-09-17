from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('shop/', views.Product_list, name='shop'),
    path('add_product/', views.add_product, name='add_product'),
    path('product_delete/<int:pk>/', views.product_delete, name='product_delete'),
    path('edit_product/<int:pk>/', views.edit_product, name='edit_product'),
    path('edit_order/<int:pk>/', views.edit_order, name='edit_order'),
]
