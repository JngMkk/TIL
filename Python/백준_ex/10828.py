# https://www.acmicpc.net/problem/10828

import sys
input = sys.stdin.readline
lst = []
n = int(input())
for i in range(n):
    inp = input().split()
    if inp[0] == 'push':
        lst.append(int(inp[1]))
    elif inp[0] == 'top':
        if len(lst) == 0:
            print(-1)
        else:
            print(lst[-1])
    elif inp[0] == 'size':
        print(len(lst))
    elif inp[0] == 'empty':
        if len(lst) == 0:
            print(1)
        else:
            print(0)
    elif inp[0] == 'pop':
        if len(lst) == 0:
            print(-1)
        else: 
            print(lst.pop())
    else:
        continue