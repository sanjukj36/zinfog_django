from django.shortcuts import render, redirect
from .models import Product
from .form import ProductForm,OrderForm
from django.contrib import messages
from Customer.models import Order

# Create your views here.

def Product_list(request):
    products=Product.objects.all()
    order = Order.objects.all()
    return render(request, 'shop/Product_list.html',{'products':products,"order":order})
def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('shop')
    else:
        form = ProductForm()
    return render(request, 'shop/add_product.html',{'form':form})

def product_delete(request, pk):
        try:
            product = Product.objects.get(id=pk)
            product.delete()
            messages.success(request, 'Prescription Deleted successfully')
        except Product.DoesNotExist:
            messages.error(request, 'Product does not exist')
        except Exception as e:
            messages.error(request, f'Error: {e}')

        return redirect('shop')


def edit_product(request, pk):

    product = Product.objects.get(pk=pk)

    form = ProductForm(instance=product)

    if request.method == "POST":
        form = ProductForm(request.POST, instance=product)

        if form.is_valid():
            form.save()

            return redirect('shop')
    return render(request, 'shop/add_product.html', {'form': form})

def edit_order(request, pk):

    order = Order.objects.get(pk=pk)

    form = OrderForm(instance=order)

    if request.method == "POST":
        form = OrderForm(request.POST, instance=order)

        if form.is_valid():
            form.save()

            return redirect('shop')
        return redirect('shop')
    return render(request, 'shop/add_product.html', {'form': form})
