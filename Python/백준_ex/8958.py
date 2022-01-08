# https://www.acmicpc.net/problem/8958

import sys
input = sys.stdin.readline
n = range(int(input()))
for _ in n:
    s = 0
    cnt = 1
    for ox in input():
        if ox == 'O':
            s += cnt
            cnt += 1
        else:
            cnt = 1
    print(s)