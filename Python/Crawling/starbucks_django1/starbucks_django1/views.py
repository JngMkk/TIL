from django.shortcuts import render
from django.http import JsonResponse
from . import starbucks3

def index(request):
    return render(request, 'index.html')


# 오래걸리는 코드라면 먼저 따로 서버에 json파일을 만들어 놓고 받아오게.
def starbucks(request):
    lst = []
    for sc in starbucks3.getSiDo():
        lst.extend(starbucks3.getStore(sc))
    d = {'list': lst}
    return JsonResponse(d)