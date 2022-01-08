# https://www.acmicpc.net/problem/2741

import sys
input = sys.stdin.readline
n = int(input())
for i in range(1, n+1): print(i)

# 다른 방법
n = range(1, int(input()) + 1)
print('\n'.join(map(str, n)))