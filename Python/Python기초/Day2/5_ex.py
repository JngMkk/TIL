# 16진수 한글자 입력하고 16진수인지 판별
a = input('16진수 한글자 입력 :')

if '0' <= a <= '9' or 'A' <= a <= 'F' or 'a' <= a <= 'f' :
    print("10진수 ==> ", int(a, 16))
else :
    print("16진수가 아닙니다.")

# 교환할 돈 계산
c1 = c2 = c3 = c4 = c5 = c6 = c7 = c8 = 0
cash = int(input('교환할 돈은 얼마 ? '))
c1 = cash // 50000
cash %= 50000
c2 = cash // 10000
cash %= 10000
c3 = cash // 5000
cash %= 5000
c4 = cash // 1000
cash %= 1000
c5 = cash // 500
cash %= 500
c6 = cash // 100
cash %= 100
c7 = cash // 50
cash %= 50
c8 = cash // 10
cash %= 10
print(f'50000원 {c1}장, 10000원 {c2}장, 5000원 {c3}장, 1000원 {c4}장')
print(f'500원 {c5}개, 100원 {c6}개, 50원 {c7}개, 10원 {0}개')
print(f'바꾸지 못한 돈 ==> {cash}')

# 난수 발생시켜 주사위 결과
from random import randint
a = randint(1, 6)
b = randint(1, 6)
if a == b:
    msg = '비겼다.'
elif a > b:
    msg = 'A가 이겼다.'
else:
    msg = 'B가 이겼다.'
print(f'A의 주사위 숫자는 {a} 입니다.')
print(f'B의 주사위 숫자는 {b} 입니다.')
print(msg)