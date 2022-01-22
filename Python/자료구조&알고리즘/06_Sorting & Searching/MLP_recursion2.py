# 함수
def addNumber(num):
    """ 1에서 num까지 합 """
    if num <= 1:
        return 1
    return num + addNumber(num-1)

def factorial(x):
    if x <= 1:
        return 1
    return x * factorial(x-1)

def countDown(x):
    print(x)
    x -= 1
    if x < 1:
        return '발사!'
    return countDown(x)

def star(n):
    if n>0:
        star(n-1)
        print('*'*n)

def gugu(dan, num):
    print('%d x %d = %2d' % (dan, num, dan*num))
    if num < 9:
        gugu(dan, num+1)

def pow(x, n):
    if n == 0:
        return 1
    return x * pow(x, n-1)

import random
array = [random.randint(0,255) for _ in range(random.randint(10,20))]

def arySum(ary, n):
    if n <= 0:
        return array[0]
    return ary[n] + arySum(ary, n-1)


# 메인

star(5)
for dan in range(2,10):
    gugu(dan, 1)

print(pow(2, 4))

print(array)
print(arySum(array, len(array) - 1))