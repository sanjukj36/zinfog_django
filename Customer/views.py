from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist
from Shop.models import Product
from .models import Order, CartItem

from .models import CartItem
from .form import OrderForm

# Create your views here.
def Product_list(request):
    products = Product.objects.all()
    return render(request, 'customer/Product_list.html', {'products': products,})

def Cart(request, ct_items=None):
    cart = CartItem.objects.all()
    order = Order.objects.all()
    return render(request, 'customer/cart.html',{"cart":cart,'order':order})

def Add_cart(request, product_id):

    product = Product.objects.get(id=product_id)
    cart=CartItem.objects.create(product=product)
    cart.save()
    return redirect('Cart')  # Assuming 'Cart' is the name of your cart view


def create_order(request):
    if request.method == 'POST':
        address = request.POST.get('address')
        cart_items = CartItem.objects.all()
        for cart_item in cart_items:

            order_item = Order()
            order_item.name = cart_item.product.name
            order_item.price = cart_item.product.price
            order_item.Address = address
            order_item.status = "Approved"

            order_item.save()
        cart_items.delete()
        # After saving the orders, you can redirect to a success page or display a message
        return redirect('Cart')  # Assuming 'product_list' is the name of your product list view
    else:
        return render(request, 'shop/add_product.html')
