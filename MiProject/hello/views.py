from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index1(request):
    return render (request, "Hello/index.html")

def Yanna(request):
    return HttpResponse("Hello, Yanna!")

def Sam(request):
    return HttpResponse("Hello, Sam!!")

def greet(request, name):
    return HttpResponse(f"Hello, {name.capitalize()}!!! ")