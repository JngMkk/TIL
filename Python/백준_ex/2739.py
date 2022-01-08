# https://www.acmicpc.net/problem/2739

import sys
input = sys.stdin.readline
n = int(input())
for i in range(1, 10):
    print('%d * %d = %d' % (n, i, n*i))

# 숏코드
n1, n2 = int(input()), 1
exec("print(n1, '*', n2, '=', n1*n2); n2+=1;"*9)