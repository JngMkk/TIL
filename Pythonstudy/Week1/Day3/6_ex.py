for i in range(5, 0, -1):
    print('*' * i)

n = int(input('몇 층의 트리 ? '))
for i in range(1, n * 2, 2):
    print(' ' * (n - 1) + '*' * i)
    n -= 1

a = input('숫자 입력 : ')
if a == '7':
    print('7 입력 ! 종료')
else:
    while True:
        b = input('다시 입력 : ')
        if b == '7':
            print('7 입력 ! 종료')
            break

cash = 10000
cnt = 0
price = 3000
while True:
    cnt += 1
    cash -= price
    if cash < price:
        print(f'노래를 {cnt}곡 불렀습니다.')
        print(f'잔액 {cash}원')
        print(f'잔액이 부족합니다. 종료합니다.')
        break
    print(f'노래를 {cnt}곡 불렀습니다.')
    print(f'현재 {cash}원 남았습니다.')
