# https://www.acmicpc.net/problem/11657

import sys
input=sys.stdin.readline
n, m = map(int, input().split())
edges = []
INF = int(1e9)
dist = [INF] * (n+1)
for _ in range(m):
    a, b, c = map(int, input().split())
    edges.append((a, b, c))
def bf(s):
    dist[s] = 0
    for i in range(n):
        for j in range(m):
            now = edges[j][0]
            next = edges[j][1]
            cost = edges[j][2]
            if dist[now] != INF and dist[next] > dist[now] + cost:
                dist[next] = dist[now] + cost
                if i == n-1:
                    return True
    return False
ex = bf(1)
if ex:
    print("-1")
else:
    for i in range(2, n+1):
        if dist[i] == INF:
            print("-1")
        else:
            print(dist[i])
