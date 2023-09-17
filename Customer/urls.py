from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.Product_list, name='Product_list'),
    path('Cart/', views.Cart, name='Cart'),
    path('Add_cart/<int:product_id>/', views.Add_cart, name='Add_cart'),
    path('create_order', views.create_order, name='create_order'),
    # path('cartDetails/', views.cart_details, name='cartDetails'),
    # path('add/<int:product_id>/', views.add_cart, name='addcart'),
    # path('cart_decrement/<int:product_id>/', views.min_cart, name='cart_decrement'),
    # path('remove/<int:product_id>/', views.cart_delete, name='remove'),
    # path('checkout/', views.checkout, name='checkout'),
]
