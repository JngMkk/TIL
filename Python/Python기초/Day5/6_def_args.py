# 가변길이 매개변수 : *args, **kwargs
# 매개변수의 개수가 정해져 있지 않은 경우
# 여러 개의 값을 전달받아 사용할 경우

# *args : arguments의 약자, 인수 값을 받음
# **kwargs : keyWord arguments의 약자, key = value 값을 받음
def sumN(*args):
    a = 0
    for arg in args:
        a += arg
    return a

def showNames(*names):
    for n in names:
        print(n, end = ' ')
    print()

def showInfo(**kwargs):
    for k in kwargs.keys():
        print(k, end = ' ')
    print()
    for v in kwargs.values():
        print(v, end = ' ')
    print()
    for i in kwargs.items():
        print(i, end = ' ')
    print()

