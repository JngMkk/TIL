from django.shortcuts import render
from .models import MyBoard

def index(request):
    return render(request, 'index.html', {'list': MyBoard.objects.all().order_by('-id')})   # 내림차순
