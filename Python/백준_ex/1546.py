# https://www.acmicpc.net/problem/1546

n = int(input())
s = list(map(int, input().split()))
M = 100 / max(s)
for i in range(n):
    s[i] = s[i] * M
print(sum(s) / n)