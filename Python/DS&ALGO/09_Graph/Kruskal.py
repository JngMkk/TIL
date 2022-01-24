"""
신장 트리

- 그래프에서 모든 노드를 포함하면서 '사이클이 존재하지 않는 부분 그래프'를 의미(일부 간선만 이용)
    - 모든 노드가 포함되어 서로 연결되면서 사이클이 존재하지 않는다는 조건은 트리의 조건이기도 함

"""

"""
최소 신장 트리

- 최소한의 비용으로 구성되는 신장 트리를 찾아야 할 때

- 예를 들어 N개의 도시가 존재하는 상황에서 두 도시 사이에 도로를 놓아 전체 도시가 서로 연결될 수 있게 도로를 설치하는 경우
    - 두 도시 A, B를 선택했을 때 A에서 B로 이동하는 경로가 반드시 존재하도록 도로를 설치함

"""

"""
Kruskal Algorithm

- 대표적인 최소 신장 트리 알고리즘

- 그리디 알고리즘으로 분류

- 구체적인 동작 과정
    1. 간선 데이터를 비용에 따라 오름차순으로 정렬
    2. 간선을 하나씩 확인하며 현재의 간선이 사이클을 발생시키는지 확인
        1. 사이클이 발생하지 않는 경우 최소 신장 트리에 포함
        2. 사이클이 발생하는 경우 최소 신장 트리에 포함시키지 않음
    3. 모든 간선에 대해 2번의 과정을 반복

- 성능
    - 간선의 개수가 E개일 때, O(ElogE)의 시간 복잡도를 가짐
    - 가장 많은 시간을 요구하는 곳은 간선의 정렬을 수행하는 부분
        - 표준 라이브러리를 이용해 E개의 데이터를 정렬하기 위한 시간 복잡도는 O(ElogE)

"""

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

"""
입력 예제

7 9
1 2 29
1 5 75
2 3 35
2 6 34
3 4 7
4 6 23
4 7 13
5 6 53
6 7 25

"""

v, e = map(int, input().split())
parent = [0] * (v+1)
edges = []

for i in range(1, v+1):
    parent[i] = i

for _ in range(e):
    a, b, cost = map(int, input().split())
    edges.append((cost, a, b))                              # 비용 순으로 정렬하기 위해 튜플의 첫 번째 원소를 비용으로 설정

edges.sort()                                                # 간선의 비용을 오름차순으로 정렬

result = 0
for edge in edges:
    cost, a, b = edge
    if find_parent(parent, a) != find_parent(parent, b):    # 사이클이 발생하지 않는 경우에만 집합에 포함
        union_parent(parent, a, b)
        result += cost

print(result)