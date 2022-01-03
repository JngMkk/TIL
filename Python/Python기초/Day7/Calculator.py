# 사칙연산 함수 작성
# 모듈로 실행하려면 파일이름이 숫자로 시작하면 안됨
def add(a, b):
    c = a + b
    return c
def sub(a, b):
    c = a - b
    return c
def mul(a, b):
    c = a * b
    return c
def div(a, b):
    c = a / b
    return c
def mod(a, b):
    c = a % b
    return c

if __name__ == '__main__':
    print('Calculator')
else:
    print('No!')

print(mul(5, 5))        # Calculator
                        # 25