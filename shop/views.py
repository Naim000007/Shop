from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
from math import ceil

# Create your views here.
def index(request):
    products = Product.objects.all()
    print(products)
    n = len(products)
    nslides = n//4 + ceil((n/4)-(n//4))
    params = {'no_of_slides':nslides, "range":range(1, nslides), 'product':products}
    return render (request, 'shop/index.html',params)

def about(request):
    return render(request, "shop/about.html")

def contact(request):
    return HttpResponse("contact")

def tracker(request):
    return HttpResponse("tracker")

def checkout(request):
    return HttpResponse("checkout")

def productView(request):
    return HttpResponse("productView")


def search(request):
    return HttpResponse("search")
