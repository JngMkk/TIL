"""
다익스트라 개선된 구현 방법

- 우선순위 큐 사용해 구현
    - 우선순위가 가장 높은 데이터를 가장 먼저 삭제
    - 대부분의 프로그래밍 언어에서 표준 라이브러리 형태로 지원
    - 우선순위 큐를 구현하기 위해 힙 사용
        - 우선순위 큐 구현 방식
            - 리스트는 삽입 O(1) 삭제 O(N)
            - 힙은 O(logN) 삭제 O(logN)

- 매 단계마다 방문하지 않은 노드 중에서 최단 거리가 가장 짧은 노드를 선택하기 위해 힙 자료구조를 이용

- 다익스트라 알고리즘이 동작하는 기본 원리는 동일
    - 현재 가장 가까운 노드를 저장해 놓기 위해서 힙 자료구조를 추가적으로 이용한다는 점이 다름
    - 현재의 최단 거리가 가장 짧은 노드를 선택해야 하므로 최소 힙 사용

- 성능
    - 힙 자료구조를 이용하는 다익스트라 알고리즘의 시간 복잡도는 O(ElogV)
    - 노드를 하나씩 꺼내 검사하는 반복문(while문)은 노드의 개수 V 이상의 횟수로는 처리되지 않음(방문된 노드는 무시하므로)
        - 결과적으로 현재 우선순위 큐에서 꺼낸 노드와 연결된 다른 노드들을 확인하는 총 횟수는
          최대 간선의 개수(E)만큼 연산이 수행될 수 있음
    - 직관적으로 전체 과정은 E개의 원소를 우선순위 큐에 넣었다가 모두 빼내는 연산과 매우 유사함
        - 시간 복잡도를 O(ElogE)로 판단할 수 있음
        - 중복 간선을 포함하지 않는 경우에 이를 O(ElogV)로 정리할 수 있음
            - O(ElogE) -> O(ElogV^2) -> O(2ElogV) -> O(ElogV)

"""

import heapq
import sys

input = sys.stdin.readline
inf = int(1e9)

n, m = map(int, input().split())
start = int(input())
graph = [[] for _ in range(n+1)]
distance = [inf] * (n+1)

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

def dijkstra(start):
    q = []
    heapq.heappush(q, (start, 0))                   # 시작 노드로 가기 위한 최단 경로는 0으로 설정하여, 큐에 삽입 (노드, 거리) 튜플 형태
    distance[start] = 0
    while q:                                        # 큐가 비어있지 않다면
        now, dist = heapq.heappop(q)                # 가장 최단 거리가 짧은 노드에 대한 정보 꺼내기
        if distance[now] < dist:                    # 현재 노드가 이미 처리된 적이 있는 노드라면 무시
            continue
        for i in graph[now]:                        # 현재 노드와 연결된 다른 인접한 노드들을 확인
            cost = dist + i[1]
            if cost < distance[i[0]]:               # 현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧은 경우
                distance[i[0]] = cost
                heapq.heappush(q, (i[0], cost))

"""
입력 예제

6 11
1
1 2 2
1 3 5
1 4 1
2 3 3
2 4 2
3 2 3
3 6 5
4 3 3
4 5 1
5 3 1
5 6 2

"""

# 테스트
dijkstra(start)

for i in range(1, n+1):
    if distance[i] == inf:
        print("infinity")
    else:
        print(distance[i])