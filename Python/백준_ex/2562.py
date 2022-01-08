# https://www.acmicpc.net/problem/2562

a = []
for _ in range(9):
    a.append(int(input()))
print(max(a), a.index(max(a))+1, sep='\n')