# 파이썬 딕셔너리를 이용한 구현


d = {}
d['data'] = '자료'
d['structure'] = '구조'
print('나의 단어장:')
print(d)
if d.get('game'): 
    print('탐색 : game -->', d['game'])
if d.get('data'): 
    print('탐색 : data --> ', d['data'])

d.pop('data')
print('나의 단어장:')
print(d)