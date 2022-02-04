from django.shortcuts import render, redirect

# Create your views here.

def index(request):
    return render(request, "var_app/index.html")

def variables01(request):
    my_list = ['python', 'django', 'templates']
    return render(request, "var_app/variables01.html", {"lst":my_list})

def variables02(request):
    my_dict = {'class': 'multi', 'name': 'hong-gd'}
    return render(request, 'var_app/variables02.html', {'dct' : my_dict})

def forloop(request):
    return render(request, 'var_app/forloop.html', {"number": range(1,11)})

def if1(request):
    return render(request, 'var_app/if1.html', {'user':{'id':'kim-sd', 'job':'student'}})

def if2(request):
    return render(request, 'var_app/if2.html', {'role': 'manager', 'id': 'multi'})

def href(request):
    return render(request, 'var_app/href.html')

def get_post(request):
    if request.method == 'GET':
        return render(request, 'var_app/get.html')
    elif request.method == 'POST':
        return render(request, 'var_app/post.html')
    else:
        return redirect('index')