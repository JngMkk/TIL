# * : 변수 앞에 붙은 경우 *args, **kwagrs -> unpacking
def asterisk_test(a, *args):
    print(a, args)
    print(type(args))

asterisk_test(1, 2, 'hi', True)     # args : 튜플 형태로 반환

def asterisk_test2(a, *args):
    print(a, *args)
    print(type(args))

asterisk_test2(1, 2, 'hi', True)    # 1 2 hi True (unpacking)

a, b, c = [1, 2, 3]
print(a, b, c)          # 1 2 3 (unpacking)

a, b, c = ([1, 2, 3], [3, 4, 5], [5, 6, 7])
print(a, b, c)          # [1, 2, 3] [3, 4, 5] [5, 6, 7] (unpacking)

data = ([1, 2, 3], [3, 4, 5], [5, 6, 7])
print(*data)            # unpacking

def asterisk_test3(a, **kwagrs):
    print(a, kwagrs)
    print(type(kwagrs))

asterisk_test3(1, b = 2, c = 'hi', d = True)    # kwargs : 딕셔너리 형태로 반환

def asterisk_test4(a, **kwagrs):
    print(a, *kwagrs)       # unpacking
    print(type(kwagrs))

asterisk_test4(1, b = 2, c = 'hi', d = True)

data2 = {'b' : 2, 'c' : 'hi', 'd' : True}
asterisk_test3(1, **data2)  # 딕셔너리
print(*data2.items())       # unpacking -> 튜플