from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Product, Order
from .forms import ProductForm, OrderForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.db.models import Sum, Value
from django.db.models.functions import Coalesce


# Create your views here.

@login_required
def index(request):
    orders = Order.objects.all()
    products = Product.objects.all()
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.staff = request.user
            instance.save()
            return redirect('dashboard-index')
    else:
        form = OrderForm()    
    context={
        'orders':orders,
        'form':form,
        'products':products,
    }
    return render(request, 'dashboard/index.html', context)

@login_required
def staff(request):
    workers = User.objects.all()
    context={
        'workers':workers,
    }
    return render(request, 'dashboard/staff.html', context)

@login_required
def staff_detail(request, pk):
    workers = User.objects.get(id=pk) 
    context={
        'workers':workers,
    }
    return render(request, 'dashboard/staff_detail.html', context)

@login_required
def product(request):
    items = Product.objects.all() # USING ORM 
    #items = Product.objects.raw('SELECT * FROM dashboard_product')


    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            product_name = form.cleaned_data.get('name')
            messages.success(request, f'{product_name} has been added.')
            return redirect('dashboard-product')
    else:
        form = ProductForm()


    context={
        'items':items,
        'form':form,
    }
    return render(request, 'dashboard/product.html', context)

@login_required
def product_delete(request, pk):
    item = Product.objects.get(id=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('dashboard-product')
    return render(request, 'dashboard/product_delete.html')

@login_required
def product_update(request, pk):
    item = Product.objects.get(id=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('dashboard-product')
    else:
        form = ProductForm(instance=item)
    context = {
        'form':form,
    }
    return render(request, 'dashboard/product_update.html', context)

@login_required
def order(request):
    orders = Order.objects.all()

    context = {
        'orders':orders,
    }
    return render(request, 'dashboard/order.html', context)

from django import template

register = template.Library()

@login_required
def total_quantity(products):
    return sum(getattr(product, 'product_quantity') for product in products)

@login_required
def index(request):
    # Fetch all orders
    orders = Order.objects.all()

    # Fetch all products and annotate them with total sold quantity
    products = Product.objects.annotate(
        total_sold=Coalesce(Sum('order__order_quantity'), Value(0))
    )

    # Find the most and least sold products
    most_sold_product = products.order_by('-total_sold').first()
    least_sold_product = products.order_by('total_sold').first()

    # Handle order form submission
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.staff = request.user
            instance.save()
            return redirect('dashboard-index')
    else:
        form = OrderForm()

    # Context to pass to the template
    context = {
        'orders': orders,
        'form': form,
        'products': products,
        'most_sold_product': most_sold_product,
        'least_sold_product': least_sold_product,
    }

    return render(request, 'dashboard/index.html', context)

def landing_page(request):
    return render(request, 'dashboard/landingpage.html')

def login_page(request):
    return render(request, 'login.html')  # Ensure 'login.html' exists in your templates