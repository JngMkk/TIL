# https://www.acmicpc.net/problem/2753

import sys
input = sys.stdin.readline
yr = int(input())
if yr % 4 == 0 and (yr % 100 != 0 or yr % 400 == 0):
    print(1)
else:
    print(0)
