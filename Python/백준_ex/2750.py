# https://www.acmicpc.net/problem/2750

import sys
input = sys.stdin.readline

# n = int(input())
# s = set()
# for i in range(n):
#     s.add(int(input()))
# for i in sorted(s):
#     print(i)

n = int(input())
lst = []
for i in range(n):
    lst.append(int(input()))
for i in range(len(lst)):
    for j in range(i+1, len(lst)):
        if lst[i] > lst[j]:
            lst[i], lst[j] = lst[j], lst[i]
for i in lst:
    print(i)