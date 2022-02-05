# https://www.acmicpc.net/problem/11279

import sys
import heapq

input=sys.stdin.readline
h=[]
for _ in range(int(input())):
    n = int(input())
    if n == 0:
        if not h:
            print(0)
        else:
            print(abs(heapq.heappop(h)))
    else:
        heapq.heappush(h, -n)