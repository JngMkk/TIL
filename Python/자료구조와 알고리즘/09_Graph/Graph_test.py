# DFS
def DFS(graph, start, visited = set()):     # 처음 호출할 때 visited 공집합
    if start not in visited:                # start가 방문하지 않은 정점이면
        visited.add(start)                  # start를 방문한 노드 집합에 추가
        print(start, end = ' ')             # start를 방문했다고 출력
        nbr = graph[start] - visited        # nbr : 차집합 연산 이용
        for v in nbr:                       # v is an element {인접정점} - {방문정점}
            DFS(graph, v, visited)          # v에 대해 DFS를 순환적으로 호출


import collections
# BFS
def BFS(graph, start):                      
    visited = set([start])                  # 맨 처음엔 start만 방문한 정점
    queue = collections.deque([start])      # 컬렉션의 덱 객체 생성(Queue로 사용)
    while queue:                            # 공백이 아닐 때까지
        vertex = queue.popleft()            # Queue에서 하나의 정점 vertex를 빼냄
        print(vertex, end = ' ')            # vertex는 방문했음을 출력
        nbr = graph[vertex] - visited       # nbr : 차집합 연산 이용
        for v in nbr:                       # v is an element {인접정점} - {방문정점}
            visited.add(v)                  # v는 방문했음
            queue.append(v)                 # v를 Queue에 삽입


# 연결 성분 검사 알고리즘
def find_connected_component(graph):
    visited = set()                                     # 이미 방문한 정점 집합
    colorList = []                                      # 부분 그래프별 정점 리스트 
    for vtx in graph:                                   # 그래프의 모든 정점들에 대해
        if vtx not in visited:                          # 방문하지 않은 정점이 있다면
            color = dfs_cc(graph, [], vtx, visited)     # 새로운 컬러 리스트
            colorList.append(color)                     # 새로운 리스트 추가
    print('그래프 연결성분 개수 = %d' % len(colorList))
    print(colorList)
def dfs_cc(graph, color, vertex, visited):
    if vertex not in visited:                           # 아직 칠해지지 않은 정점에 대해
        visited.add(vertex)                             # 방문했음
        color.append(vertex)                            # 같은 색의 정점 리스트에 추가
        nbr = graph[vertex] - visited                   # nbr : 차집합 연산 이용
        for v in nbr:                                   # v is an element {인접정점} - {방문정점}
            dfs_cc(graph, color, v, visited)            # 순환 호출
    return color                                        # 같은 색의 정점 리스트 반환


# 테스트
mygraph = { "A" : set(["B","C"]),
            "B" : set(["A"]),
            "C" : set(["A"]),
            "D" : set(["E"]),
            "E" : set(["D"])
          }
print('find_connected_component :')
find_connected_component(mygraph)


# 신장트리 알고리즘
import collections

def bfsST(graph, start):
    visited = set([start])                              # 맨 처음 start만 방문한 정점
    queue = collections.deque([start])                  # 컬렉션의 덱 생성(큐로 사용)
    while queue:                                        # 공백이 아닐 때까지
        v = queue.popleft()                             # 큐에서 하나의 정점 v를 빼냄
        nbr = graph[v] - visited                        # nbr = {v의 인접정점} - {방문정점}
        for u in nbr:                                   # 갈 수 잇는 모든 인접 정점에 대해
            print("(", v, ",", u, ")", end = "")        # (v, u) 간선 추가
            visited.add(u)                              # u는 방문했음.
            queue.append(u)                             # u를 큐에 삽입

# 위상정렬 알고리즘
def topological_sort_AM(vertex, graph):
    n = len(vertex)
    inDeg = [0] * n                         # 정점의 진입차수 저장
    for i in range(n):
        for j in range(n):
            if graph[i][j] > 0:
                inDeg[j] += 1               # 진입차수를 1 증가시킴
    vlist = []                              # 진입차수가 0인 정점 리스트를 만듦
    for i in range(n):
        if inDeg[i] == 0:
            vlist.append(i)
    while len(vlist) > 0:                   # 리스트가 공백이 아닐 때까지
        v = vlist.pop()                     # 진입차수가 0인 정점을 하나 꺼냄
        print(vertex[v], end = ' ')
        for u in range(n):
            if v != u and graph[v][u] > 0:
                inDeg[u] -= 1               # 연결된 정점의 진입차수 감소
                if inDeg[u] == 0:           # 진입차수가 0이면
                    vlist.append(u)         # vlist에 추가

vertex =    ['A', 'B', 'C', 'D', 'E', 'F']
graphAM = [ [ 0,   0,   1,   1,   0,   0 ],
            [ 0,   0,   0,   1,   1,   0 ],
            [ 0,   0,   0,   1,   0,   1 ],
            [ 0,   0,   0,   0,   0,   1 ],
            [ 0,   0,   0,   0,   0,   1 ],
            [ 0,   0,   0,   0,   0,   0 ] ]
print('topological_sort: ')
topological_sort_AM(vertex, graphAM)
print()