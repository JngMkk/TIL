from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, "var/index.html")

def variables01(request):
    my_list = ['python', 'django', 'templates']
    return render(request, "var/variables01.html", {"lst":my_list})