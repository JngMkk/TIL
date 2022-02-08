from django.shortcuts import render, redirect
from .forms import MyMemberForm

def index(request):
    return render(request, 'index.html')

def register(request):
    if request.method == "POST":
        form = MyMemberForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        return render(request, 'register.html', {'form': MyMemberForm()})

def result(request):
    return render(request, 'result.html')