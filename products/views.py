from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
from django.shortcuts import redirect

def index(request):
    products = Product.objects.all()
    return render(request, 'index.html', 
                            {'products': products})

def redirectProducts(request):
    return redirect('productsListUrl', permanent=True)#ссылка, заданная в urls.py 