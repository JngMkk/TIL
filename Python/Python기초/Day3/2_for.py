# 반복문
sum1 = 0
for i in range(1, 11):
    sum1 += i
print(sum1)

sum1 = 0
for i in range(1, 100, 2):
    sum1 += i
print(sum1)

sum1 = sum2 = 0
for i in range(1, 101):
    if i % 2 == 1:
        sum1 += i
    else:
        sum2 += i
print(sum1, sum2)

sum1 = sum2 = 0
for i in range(1, 101, 2):
    sum1 += i
    sum2 += i + 1
print(sum1, sum2)

sum1 = 0
for i in range(3, 101, 3):
    print(i)
    sum1 += i
print(sum1)

# 구구단
dan = int(input('구구단 단 입력: '))
for n in range(1, 10):
    print('%d x %d = ' % (dan, n), dan * n)

# 카운트다운
count = int(input('시작 숫자를 입력하시오 : '))
for i in range(count, 0, -1):
    print(i, end = ' ')
print('성공')

# 반복문 성적
score = [70, 90, 100, 50, 85]
idx = 0
for i in score:
    idx += 1
    if i >= 60:
        print(f'{idx}번 학생 합격')
    else:
        print(f'{idx}번 학생 불합격')

score = [70,90,100,50,85]
for i, score in enumerate(score):
    index = i + 1
    if score >= 60:
        print(f'{index}번 학생 합격')
    else:
        print(f'{index}번 학생 불합격')

# 부호
p = m = z = 0
for i in range(1, 11):
    a = int(input(f'숫자{i} 입력 : '))
    if a > 0:
        p += 1
    elif a < 0:
        m += 1
    else:
        z += 1
print('----------------')
print('양의 개수 : ', p)
print('음의 개수 : ', m)
print('0의 개수 : ', z)

"""
1 2 3 4
5 6 7 8
9 10 11 12

출력하기
"""
n = 1
for _ in range(3):
    for i in range(n, n + 4):
        print(i, end = ' ')
    print()
    n += 4

n = 0
for _ in range(3):
    for i in range(4):
        n += 1
        print(n, end = ' ')
    print()

for i in range(3):
    for j in range(1, 5):
        print(j + i * 4, end = ' ')
    print()