# https://www.acmicpc.net/problem/2577

a = int(input())
b = int(input())
c = int(input())
for i in range(10):
    print(list(map(int, str(a*b*c))).count(i))