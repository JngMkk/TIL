from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# SSR (Server Side Rendering) / CSR (Client Side Rendering)
def index(request):
    return HttpResponse("<h1><a href='/hello01/test'>Hello, Django</h1>")

def test(request):
    return HttpResponse("<h1><a href='/hello01/'>return</a></h1>")

def my(request):
    return HttpResponse("<h1>JoongMo</h1>")