# 추상 자료형
# 프로그래머가 추상적으로 정의한 자료형
# 예) Bag의 추상 자료형

def contains(bag, e):
    return e in bag

def insert(bag, e):
    bag.append(e)

def remove(bag, e):
    bag.remove(e)

def count(bag):
    return len(bag)

myBag = []
insert(myBag, '휴대폰')
insert(myBag, '지갑')
print('가방 속 물건:', myBag)

insert(myBag, '손수건')
print('가방 속 물건:', myBag)


# 실행시간 측정
import time

myBag = []
start = time.time()
insert(myBag, '축구공')
insert(myBag, '손수건')
insert(myBag, '휴대폰')
insert(myBag, '지갑')
remove(myBag, '축구공')
end = time.time()
print('실행시간 =', end-start)

# Bagclass
class Bag:
    def __init__(self, contain, insert, remove, count):
        self.contain = contain
        self.insert = insert
        self.remove = remove
        self.count = count
    
    def contain(self, e):
        return e in self
    def insert(self, e):
        self.append(e)
    def remove(self, e):
        self.remove(e)
    def count(self):
        return len(self)

Mybag = []
Bag.insert(Mybag, 'Hi')
print(Mybag)

# 팩토리얼 구하기
# 순환구조 : n! = n * (n - 1)!
# 반복구조 : n! = n * (n - 1) * (n - 2) * ... * 1
# 이 경우 순환과 반복의 수행속도에는 차이가 없다 O(n)

# 순환구조
n = int(input('숫자입력 : '))
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(5))

# 순환이 더 빠른 예 : 거듭제곱 계산

# 반복구조
# 내부 반복문 : O(n)
def power_iter(x, n):
    result = 1.0
    if n == 0:
        return 1
    else:
        for _ in range(n):
            result = result * x
        return result

# 시간 복잡도
# 순환 함수 : O(log2의n)
# 순환구조
def power(x, n):
    if n == 0:
        return 1
    elif (n % 2) == 0:  
        return power(x * x, n / 2)  # n이 짝수
    else:
        return x * power(x * x, (n - 1) // 2)   # n이 홀수
# 순환이 느린 예 : 피보나치 수열
# 피보나치 수열 : 0, 1, 1, 2, 3, 5, 8, 13, 21, ...

# 순환구조
# 같은 항이 중복해서 계산됨
# n이 커지면 더욱 심각
# 시간 복잡도 : O(2^n)
def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)

# 반복구조
# 시간복잡도 : O(n)
def fib_iter(n):
    if n < 2:
        return n
    last = 0
    current = 1
    for i in range(2, n + 1):
        tmp = current
        current += last
        last = tmp
    return current

# 하노이 타워 구현

# 순환을 이용
def hanoi_tower(n, fr, tmp, to):
    if n == 1:
        print('원판 1: %s --> %s' % (fr, to))
    else:
        hanoi_tower(n - 1, fr, to, tmp)
        print('원판 %d: %s --> %s' % (n, fr, to))
        hanoi_tower(n - 1, tmp, fr, to)


hanoi_tower(4, 'A', 'B', 'C')