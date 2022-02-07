from django.shortcuts import render
from .models import MyBoard

def index(request):
    return render(request, 'index.html', {'list': MyBoard.objects.all()})

def detail(request, id):
    return render(request, 'detail.html', {'dto': MyBoard.objects.get(id=id)})