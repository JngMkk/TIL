try:
    print('hi')     # 에러 가능성 있는 문장
except:             # as e
    pass            # 에러가 발생하면 처리하는 문장
else:
    pass            # 에러가 발생하지 않으면 처리하는 문장
finally:
    pass            # 에러와 상관없이 항상 수행하는 문장

try:
    f = open('hi.txt', 'r')
    d = f.read()
    print(d)
    f.close()
except FileNotFoundError as e:
    print('No!', e)
finally:
    print('Go away!')