# https://www.acmicpc.net/problem/2884

import sys
input = sys.stdin.readline
h, m = map(int, input().split())
m -= 45
if m < 0: h -= 1
print(h%24, m%60)