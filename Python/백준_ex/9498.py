# https://www.acmicpc.net/problem/9498

import sys
input = sys.stdin.readline
num = int(input())
if num >= 90:
    print('A')
elif num >= 80:
    print('B')
elif num >= 70:
    print('C')
elif num >= 60:
    print('D')
else:
    print('F')