from django.shortcuts import render, redirect
from django.core.paginator import Paginator 

# Create your views here.
from .models import Product, Cart

def index(request):
    product_objects = Product.objects.all()
    
    #Search Code 
    item_name = request.GET.get('item_name')
    if item_name != '' and item_name  is not None:
        product_objects = product_objects.filter(title__icontains= item_name)
    #paginaator page 
    paginator = Paginator(product_objects, 4)
    page = request.GET.get('page')
    product_objects = paginator.get_page(page)
    context = {'product_objects':product_objects}
    return render(request, 'index.html',context)

def detail(request, id):
    product_object = Product.objects.get(id=id)
    context = {'product_object': product_object}
    return render(request, 'detail.html',context)

def checkout(request):
    return render (request, 'checkout.html', {})






    


 