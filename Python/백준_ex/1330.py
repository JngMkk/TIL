# https://www.acmicpc.net/problem/1330

import sys
input = sys.stdin.readline
n1, n2 = map(int, input().split())
if n1 > n2:
    print('>')
elif n1 < n2:
    print('<')
else:
    print('==')