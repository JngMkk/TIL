import sys
input=sys.stdin.readline
n = int(input())
stk = []
for i in range(n):
    inp = input().split()
    if inp[0] == 'push':
        stk.append(inp[1])
    elif inp[0] == 'pop':
        if len(stk) == 0:
            print(-1)
        else:
            print(stk.pop())
    elif inp[0] == 'size':
        print(len(stk))
    elif inp[0] == 'empty':
        if len(stk) == 0:
            print(1)
        else:
            print(0)
    elif inp[0] == 'top':
        if len(stk) == 0:
            print(-1)
        else:
            print(stk[-1])
    else:
        continue

    