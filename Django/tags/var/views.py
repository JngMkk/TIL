from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, "var/index.html")

def variables01(request):
    my_list = ['python', 'django', 'templates']
    return render(request, "var/variables01.html", {"lst":my_list})

def variables02(request):
    my_dict = {'class': 'multi', 'name': 'hong-gd'}
    return render(request, 'var/variables02.html', {'dct' : my_dict})

def forloop(request):
    return render(request, 'var/forloop.html', {"number": range(1,11)})

def if1(request):
    return render(request, 'var/if1.html', {'user':{'id':'kim-sd', 'job':'student'}})

def if2(request):
    return render(request, 'var/if2.html', {'role': 'manager', 'id': 'multi'})

def href(request):
    return render(request, 'var/href.html')