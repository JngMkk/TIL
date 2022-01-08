# https://www.acmicpc.net/problem/1110

n = m = input()
if int(n) < 10:
    m = '0' + m
i = 0
while True:
    a = str(sum(map(int, n)))
    b = n[-1] + a[-1]
    n = b
    i += 1
    if n == m:
        print(i)
        break

# 다른 방법
n = int(input())
m = n
i = 0
while True:
    m = m % 10 * 10 + (m % 10 + m // 10) % 10
    i += 1
    if m == n:
        print(i)
        break