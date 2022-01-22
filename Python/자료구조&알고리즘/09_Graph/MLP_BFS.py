"""
BFS(너비 우선 탐색)

. 그래프에서 가까운 노드부터 우선적으로 탐색하는 알고리즘
. 큐 자료구조 이용
    - 탐색 시작 노드를 큐에 삽입하고 방문 처리를 함
    - 큐에서 노드를 꺼낸 뒤에 해당 노드의 인접 노등 중에서
      방문하지 않은 노드를 '모두' 큐에 삽입하고 방문처리함
    - 더 이상 2번의 과정을 수행할 수 없을 때까지 반복
. 각 간선의 비용이 모두 동일한 상황에서 최단거리 문제 해결 가능

"""

# 큐(Queue) 구현을 위해 deque 라이브러리 사용
from collections import deque

# BFS 메서드 정의
def bfs(graph, s, visited):
    queue = deque([s])
    # 현재 노드를 방문 처리
    visited[s] = True
    # 큐가 빌 때까지 반복
    while queue:
        # 큐에서 하나의 원소를 뽑아 출력
        v = queue.popleft()
        print(v, end = ' ')
        # 아직 방문하지 않은 인접한 원소들을 큐에 삽입
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

# 각 노드가 연결된 정보
graph = [
    [],             # 노드가 1번부터 출발하는 경우 비워둔다.
    [2, 3, 8],      # 1의 인접노드
    [1, 7],         # 2의 인접노드
    [1, 4, 5],      # 3의 인접노드
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

# 각 노드가 방문된 정보
visited = [False] * 9
bfs(graph, 1, visited)      # 1 2 3 8 7 4 5 6