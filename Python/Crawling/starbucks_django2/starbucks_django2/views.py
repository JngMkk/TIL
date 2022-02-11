from django.shortcuts import render
from django.http import JsonResponse
import requests

def index(request):
    return render(request, 'index.html')

def getSiDo(request):
    url = "https://www.starbucks.co.kr/store/getSidoList.do"
    res = requests.post(url)
    json_data = res.json()
    sido_cd = list(map(lambda x: x['sido_cd'], json_data['list']))
    sido_nm = list(map(lambda x: x['sido_nm'], json_data['list']))
    sido_dic = dict(zip(sido_cd, sido_nm))
    return JsonResponse(sido_dic)

def getGuGun(request):
    sido_code = request.GET['sido_code']
    url = 'https://www.starbucks.co.kr/store/getGugunList.do'
    res = requests.post(url, data={"sido_cd":sido_code})
    json_data = res.json()
    gugun_cd = list(map(lambda x: x['gugun_cd'], json_data['list']))
    gugun_nm = list(map(lambda x: x['gugun_nm'], json_data['list']))
    gugun_dic = dict(zip(gugun_cd, gugun_nm))
    return JsonResponse(gugun_dic)

def getStore(request):
    code = request.GET['code']
    sido_code = code if code == '17' else ''
    gugun_code = '' if code == '17' else code
    url = 'https://www.starbucks.co.kr/store/getStore.do'
    res = requests.post(url, data={
                                    "ins_lat":"37.56682",
                                    "ins_lng":"126.97865",
                                    "p_sido_cd":sido_code,
                                    "p_gugun_cd":gugun_code,
                                    "in_biz_cd":"",
                                    "set_date":""
                                    })
    store_list = res.json()['list']
    lst = []
    for store in store_list:
        d = {}
        d['s_name'] = store['s_name']
        d['tel'] = store['tel']
        d['doro_address'] = store['doro_address']
        d['lat'] = store['lat']
        d['lot'] = store['lot']
        lst.append(d)
    store_dic = {'store_list' : lst}
    return JsonResponse(store_dic)