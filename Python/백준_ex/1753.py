# https://www.acmicpc.net/problem/1753

import sys, heapq
input=sys.stdin.readline
v, e = map(int, input().split())
start = int(input())
INF = int(1e9)
cost = [INF] * (v+1)
graph = [[] for _ in range(v+1)]
for _ in range(e):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
q = []
cost[start] = 0
heapq.heappush(q, (0, start))
while q:
    dist, now = heapq.heappop(q)
    if cost[now] < dist:
        continue
    for i,j in graph[now]:
        c = dist + j
        if c < cost[i]:
            cost[i] = c
            heapq.heappush(q, (c, i))
for i in range(1, v+1):
    print("INF" if cost[i]==INF else cost[i])