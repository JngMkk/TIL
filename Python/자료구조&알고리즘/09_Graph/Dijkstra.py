"""
최단 경로 문제

- 최단 경로 알고리즘은 가장 짧은 경로를 찾는 알고리즘

- 다양한 문제 상황
    - 한 지점에서 다른 한 지점까지의 최단 경로
    - 한 지점에서 다른 모든 지점까지의 최단 경로
    - 모든 지점에서 다른 모든 지점까지의 최단 경로

- 각 지점은 그래프에서 노드로 표현

- 지점 간 연결된 도로는 그래프에서 간선으로 표현

"""

"""
다익스트라 최단 경로 알고리즘

- 특정한 노드에서 출발하여 다른 모든 노드로 가는 최단 경로를 계산

- 다익스트라 최단 경로 알고리즘은 음의 간선이 없을 때 정상적으로 동작
    - 현실 세계의 도로(간선)은 음의 간선으로 표현되지 않음

- 다익스트라 최단 경로 알고리즘은 그리디 알고리즘으로 분류됨
    - 매 상황에서 방문하지 않는 노드 중 가장 비용이 적은 노드를 선택해 임의의 과정을 반복

- 동작 과정
    1. 출발 노드 설정
    2. 최단 거리 테이블 초기화
    3. 방문하지 않는 노드 중에서 최단 거리가 가장 짧은 노드 선택
    4. 해당 노드를 거쳐 다른 노드로 가는 비용을 계산하여 최단 거리 테이블을 갱신
    5. 위 과정에서 3번과 4번 반복

- 알고리즘 동작 과정에서 최단 거리 테이블은 각 노드에 대한 현재까지의 최단 거리 정보를 가지고 있음

- 처리 과정에서 더 짧은 경로를 찾으면 '이제부터는 이 경로가 제일 짧은 경로야'라고 갱신함

- 단계를 거치며 한 번 처리된 노드의 최단 거리는 고정되어 더이상 바뀌지 않음
    - 한 단계당 하나의 노드에 대한 최단 거리를 확실히 찾는 것으로 이해할 수 있음

- 다익스트라 알고리즘을 수행한 뒤에 테이블에 각 노드까지의 최단 거리 정보가 저장됨
    - 완벽한 형태의 최단 경로를 구하려면 소스코드에 추가적인 기능을 더 넣어야 함

- 간단한 구현 방법
    - 단계마다 방문하지 않은 노드 중에서 최단 거리가 가장 짧은 노드를 선택하기 위해
      매 단계마다 1차원 테이블의 모든 원소를 확인(순차 탐색)함

"""

import sys

input = sys.stdin.readline
inf = int(1e9)      # 무한을 의미하는 값으로 10억을 설정

n, m = map(int, input().split())        # 노드의 개수, 간선의 개수 입력받기
start = int(input())                    # 시작 노드 번호 입력받기
graph = [[] for _ in range(n+1)]        # 각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트 만들기
visited = [False] * (n+1)               # 방문한 적이 있는지 체크하는 목적의 리스트를 만들기
distance = [inf] * (n+1)                # 최단 거리 테이블을 모두 무한으로 초기화

for _ in range(m):                      # 모든 간선 정보 입력받기
    a, b, c = map(int, input().split())
    graph[a].append((b, c))             # a번 노드에서 b번 노드로 가는 비용이 c

# 방문하지 않은 노드 중에서, 가장 최단 거리가 짧은 노드의 번호를 반환
def get_smallest_node():
    min_value = inf
    index = 0                           # 가장 최단 거리가 짧은 노드(인덱스)
    for i in range(1, n+1):
        if distance[i] < min_value and not visited[i]:
            min_value = distance[i]
            index = i
    return index

def dijkstra(start):
    distance[start] = 0                 # 시작 노드 초기화
    visited[start] = True
    for i in graph[start]:
        distance[i[0]] = i[1]           # i -> (x, y) i[0] : 인접 노드, i[1] : 인접 노드로 가는 비용
    for _ in range(n-1):                # 시작 노드를 제외한 전체 (n-1)개의 노드에 대해 반복
        now = get_smallest_node()       # 현재 최단 거리가 가장 짧은 노드를 꺼내서,
        visited[now] = True             # 방문 처리
        for j in graph[now]:            # 현재 노드와 연결된 다른 노드를 확인
            cost = distance[now] + j[1] # 현재 노드까지의 cost + 인접 노드로 가는 cost
            if cost < distance[j[0]]:   # 현재 노드를 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우
                distance[j[0]] = cost

# 테스트
dijkstra(start)

for i in range(1, n+1):                 # 모든 노드로 가기 위한 최단 거리를 출력
    if distance[i] == inf:              # 도달할 수 없는 경우,
        print("Infinity")               # infinity 출력
    else:                               # 도달할 수 있는 경우 거리를 출력
        print(distance[i])
