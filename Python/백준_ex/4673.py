# https://www.acmicpc.net/problem/4673

s1 = set(range(1, 10001))
s2 = set()
for i in range(1, 10001):
    for j in str(i):
        i += int(j)
    s2.add(i)
for i in sorted(s1-s2):
    print(i)