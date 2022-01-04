# 빈 dictionary : dict() / a = {}
# keys(), values(), items()
naver = {'name' : 'joongmo',
        'phone' : '010-1234-5678',
        'id' : 'abcdefg'}
print(naver.keys())
print(naver.values())
print(naver.items())

for key in naver.keys():
    print(key)

print(type(naver.keys()))
ls = list(naver.keys())
print(ls)

key = 'passwd'
if naver.get(key) is None:
    print(key + '에 대한 값이 없습니다.')

print(key in naver)

data1 = {'name' : '버섯불고기', 'class' : '한식', 'type' : '불고기','ingr' : ['소고기', '양파', '간장', '설탕']}
data2 = {'name' : '카레덮밥', 'class' : '양식', 'type' : '덮밥', 'ingr' : ['카레', '감자', '양파', '당근']}
datum = [data1, data2]

for data in datum:
    for d in data.items():
        print(d)