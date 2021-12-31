# 연습문제 1
a = int(input('정수1 입력 : '))
b = int(input('정수2 입력 : '))
c = int(input('정수3 입력 : '))

if a >= b and a >= c:
    MAX = a
elif b >= c:
    MAX = b
else:
    MAX = c
print('제일 큰 수 :', MAX)

# 연습문제 2
a = input('도형 입력(1:사각형, 2:삼각형, 3:원) : ')

if a == '1':
    b = float(input('가로 입력 : '))
    c = float(input('세로 입력 : '))
    rect = b * c
    print(f'사각형의 면적 = {rect:.2f}')
elif a == '2':
    b = float(input('밑변 입력 : '))
    c = float(input('높이 입력 : '))
    tri = b * c * 0.5
    print(f'삼각형의 면적 = {tri:.2f}')
elif a == '3':
    b = float(input('반지름 입력 : '))
    PI = 3.141592
    cir = b ** 2 * PI
    print(f'원의 면적 = {cir:.2f}')