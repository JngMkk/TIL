'''
int1 = int(input('숫자1 : '))
int2 = int(input('숫자2 : '))

print(int1 + int2)
print(int1 - int2)
print(int1 * int2)
print(int1 / int2)
'''

a = int(input('국어점수 입력: '))
b = int(input('영어점수 입력: '))
c = int(input('수학점수 입력: '))
tot = a + b + c
avg = tot / 3
print(f'총점 : {tot}')
print(f'평균 : {avg:.2f}')


weight = int(input('몸무게(kg): '))
height = int(input('키(미터): '))
bmi = (weight / height ** 2) * 10000
print(f'당신의 BMI는 {bmi:.2f}입니다.')