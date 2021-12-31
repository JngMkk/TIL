cnt = 0
while True:
    a = input(' 입력 : ')
    print(a)
    if a == 'stop':
        break
    else:
        cnt += 1
print('입력된 숫자의 개수 : ', cnt)

n = str(0)
while n != '7':
    n = input('숫자입력 : ')
print('7 입력! 종료')

while True:
    tmp = input('입력 : ')
    if tmp == 'q':
        break

