from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render (request, 'shop/index.html')


def about(request):
    return HttpResponse("about")

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
