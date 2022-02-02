k = int(input())
stk = []
for _ in range(k):
    n = int(input())
    if n == 0:
        stk.pop()
    else:
        stk.append(n)
print(sum(stk))