# -*- coding:utf-8 -*-

import requests
import json

def getSiDo():
    url = "https://www.starbucks.co.kr/store/getSidoList.do"
    res = requests.post(url)
    # json객체
    json_data = res.json()
    # sido_cd , sido_nm = [], []
    # for elem in json_data['list']:
    #     sido_cd.append(elem['sido_cd'])
    #     sido_nm.append(elem['sido_nm'])
    sido_cd = list(map(lambda x: x['sido_cd'], json_data['list']))
    sido_nm = list(map(lambda x: x['sido_nm'], json_data['list']))
    sido_dic = dict(zip(sido_cd, sido_nm))
    return sido_dic

def getGuGun(sido_code):
    url = 'https://www.starbucks.co.kr/store/getGugunList.do'
    res = requests.post(url, data={"sido_cd":sido_code})
    json_data = res.json()
    gugun_cd = list(map(lambda x: x['gugun_cd'], json_data['list']))
    gugun_nm = list(map(lambda x: x['gugun_nm'], json_data['list']))
    gugun_dic = dict(zip(gugun_cd, gugun_nm))
    return gugun_dic

def getStore(sido_code='', gugun_code=''):
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
    # s_name, tel, doro_address, lat, lot
    # {'list' : [{}, {}]}
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
        if sc != '17':
            for gc in getGuGun(sc):
                lst.extend(getStore(gugun_code=gc))
        else: lst.extend(getStore('17', ''))
    d = {'list': lst}
    data = json.dumps(d, ensure_ascii=False)
    with open(f'./starbucks_allstores.json', 'w') as f:
        f.write(data)