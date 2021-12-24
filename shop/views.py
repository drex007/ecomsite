from django.shortcuts import render

# Create your views here.
from .models import Product

def index(request):
    product_objects = Product.objects.all()
    item_name = request.GET.get('item_name')
    if item_name != '' and item_name  is not None:
        product_objects = product_objects.filter(title__icontains= item_name)
    context = {'product_objects':product_objects}
    return render(request, 'index.html',context)


 