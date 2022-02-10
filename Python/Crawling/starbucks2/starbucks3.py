# -*- coding:utf-8 -*-
import requests
import json

def getSiDo():
    url = "https://www.starbucks.co.kr/store/getSidoList.do"
    res = requests.post(url)
    json_data = res.json()
    sido_cd = list(map(lambda x: x['sido_cd'], json_data['list']))
    sido_nm = list(map(lambda x: x['sido_nm'], json_data['list']))
    sido_dic = dict(zip(sido_cd, sido_nm))
    return sido_dic

def getStore(sido_code=''):
    url = 'https://www.starbucks.co.kr/store/getStore.do'
    res = requests.post(url, data={
                                    "ins_lat":"37.6113443",
                                    "ins_lng":"127.1580072",
                                    "p_sido_cd":sido_code,
                                    "p_gugun_cd":"",
                                    "in_biz_cd":"",
                                    "set_date":"",
                                    "iend":"1000"
                                    })
    store_list = res.json()['list']
    lst=[]
    for store in store_list:
        d = {}
        d['s_name'] = store['s_name']
        d['tel'] = store['tel']
        d['doro_address'] = store['doro_address']
        d['lat'] = store['lat']
        d['lot'] = store['lot']
        lst.append(d)
    return lst

if __name__ == '__main__':
    lst = []
    for sc in getSiDo():
        lst.extend(getStore(sc))
    d = {'list': lst}
    data = json.dumps(d, ensure_ascii=False)
    with open(f'./starbucks3.json', 'w') as f:
        f.write(data)

