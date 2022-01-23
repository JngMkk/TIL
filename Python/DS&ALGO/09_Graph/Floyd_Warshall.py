"""
플로이드 워셜 알고리즘

- 모든 노드에서 다른 모든 노드까지의 최단 경로를 모두 계산

- 다익스트라 알고리즘과 마찬가지로 단계별로 거쳐 가는 노드를 기준으로 알고리즘 수행
    - 다만 매 단계마다 방문하지 않은 노드 중에 최단 거리를 갖는 노드를 찾는 과정이 필요하지 않음

- 플로이드 워셜은 2차원 테이블에 최단 거리 정보를 저장

- 플로이드 워셜 알고리즘은 다이나믹 프로그래밍 유형에 속함

- 각 단계마다 특정한 노드 k를 거쳐 가는 경우를 확인
    - a에서 b로 가는 최단 거리보다 a에서 k를 거쳐 b로 가는 거리가 더 짧은지 검사

- 점화식
    - D_ab = min(D_ab, D_ak + D_kb)

- 성능
    - 노드의 개수가 N개일 때 알고리즘 상으로 N번의 단계를 수행함
        - 각 단계마다 O(N^2)의 연산을 통해 현재 노드를 거쳐 가는 모든 경로를 고려함
    - 따라서 플로이드 워셜 알고리즘의 총 시간 복잡도는 O(N^3)임

"""

INF = int(1e9)
n = int(input())
m = int(input())
graph = [[INF] * (n+1) for _ in range(n+1)]             # 2차원 리스트(그래프 표현)

for a in range(1, n+1):                                 # 자기 자신에서 자기 자신으로 가는 비용은 0으로 초기화
    for b in range(1, n+1):
        if a == b:
            graph[a][b] = 0

for _ in range(m):
    a, b, c = map(int, input().split())                 # a에서 b로 가는 비용은 c
    graph[a][b] = c

# 점화식에 따라 플로이드 워셜 알고리즘 수행
for k in range(1, n+1):                                 # k : 거쳐가는 노드
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

"""
입력 예제

4
7
1 2 4
1 4 6
2 1 3
2 3 7
3 1 5
3 4 4
4 3 2

"""

# 테스트
for a in range(1, n+1):
    for b in range(1, n+1):
        if graph[a][b] == INF:
            print("infinity", end = " ")
        else:
            print(graph[a][b], end = " ")
    print()

