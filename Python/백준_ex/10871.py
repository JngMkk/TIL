# https://www.acmicpc.net/problem/10871

n, x = map(int, input().split())
a = [i for i in map(int, input().split())]
for i in range(len(a)):
    if a[i] < x:
        print(a[i], end =' ')
print()

# 다른 방법
n, x = map(int, input().split())
a = [i for i in input().split() if int(i) < x]
print(' '.join(a))
