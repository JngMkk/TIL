# https://www.acmicpc.net/problem/1065

x = int(input())
cnt = 0
for i in range(1,x+1):
    if i < 100:
        cnt += 1
    else:
        a = list(map(int, str(i)))
        if a[0] - a[1] == a[1] - a[2]:
            cnt += 1
print(cnt)