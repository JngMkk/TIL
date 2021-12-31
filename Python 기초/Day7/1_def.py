def count(n):
    if n >= 1:
        for i in range(n, 0, -1):
            print(i, end = ' ')
        print()
    else:
        print('1이상인 숫자를 입력하세요.')

def selfcount(n):
    if n >= 1:
        print(n, end = ' ')
        return selfcount(n - 1)
    else:
        return

# 내부 함수
# 함수가 정의된 그 범위에서만 사용
def func1(x, y):
    def func2(a, b):
        return a + b
    return func2(x, y)

# 내장함수(bulit-in functions) : 파이썬에 이미 만들어져 내장되어 있는 함수들

# all() : 모든 요소가 참이면 True
# False : 0, True : 0이 아닌 값
# iterable(반복 가능한 자료형) : 리스트, 튜플, 딕셔너리 ...
# for 반복문을 이용해서
print(all([1, 2, 3]))
print(all([0, 2, 3]))

# any() : 하나라도 참이면 True
print(any([1, 2, 3]))
print(any([0, 2, 3]))
print(any([0, 0, 0]))

# chr() : 아스키 코드 값에 해당하는 문자 반환
print(chr(95))
print(chr(55))

# ord() : 문자에 대한 아스키 코드 값 반환
print(ord(' '))
print(ord('\n'))

# divmod(a, b) : a를 b로 나눈 몫과 나머지 반환
print(divmod(10, 3))

# eval(표현식) : 표현식의 연산 결과 반환
print(eval('1 + 2'))

# filter(function, iterable)
def positive(x):
    return x > 0
print(list(filter(positive, [-1, 0, 3, 5])))

def even(x):
    if x % 2 == 0:
        return x
print(list(filter(even, [1, 2, 3])))

# map() : 리스트나 튜플, 문자열 등 반복가능한 구조의 요소별로 지정된 함수를 적용
# 원본 변경 x

# lambda
# (lambda x : x + 10)(25)
# hi = lambda x : x + 10

# zip(*iterable) : iterable에서 동일한 인덱스 요소를 추출하여 묶어서 반환
print(list(zip([1,2,3], [4,5,6])))

keys = ['apple', 'melon', 'banana']
vals = [250, 300, 400]
print(list(zip(keys, vals)))