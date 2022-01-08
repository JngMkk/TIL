# https://www.acmicpc.net/problem/4344

import sys
input = sys.stdin.readline
n = range(int(input()))
for _ in n:
    a = list(map(int, input().split()))[1:]
    m = sum(a)/len(a)
    p = sum([x > m for x in a])/len(a)*100
    print(f'{p:.3f}%')

# p = sum(map(lambda x:x>m, a))/len(a)*100