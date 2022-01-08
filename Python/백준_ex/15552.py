# https://www.acmicpc.net/problem/15552

import sys
input = sys.stdin.readline
n = int(input())
for _ in range(n):
    a, b = map(int, input().split())
    print(f'{a+b}')