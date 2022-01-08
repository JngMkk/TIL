# https://www.acmicpc.net/problem/3052

s = set()
for _ in range(10):
    s.add(int(input())%42)
print(len(s))