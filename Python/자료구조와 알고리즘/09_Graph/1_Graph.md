# 그래프

> 파이썬으로 쉽게 풀어쓴 자료구조 참고

## 그래프란?

- 연결되어 있는 객체 간의 관계를 표현하는 자료구조

- 가장 일반적인 자료구조 형태

- 오일러 문제
  -  다리를 한번만 건너서 처음 출발했던 장소로 돌아오는 문제
    - 위치 : 정점(Node), 다리 : 간선(edge)
  - 오일러 정리
    - 모든 정점에 연결된 간선의 수가 짝수이면 오릴러 경로 존재함

- 그래프 G는 (V, E)로 표시
  - 정점(Vertices) 또는 노드
  - 간선(Edge) 또는 링크
    - 정점들 간의 관계 의미

1. 그래프의 종류

   - 간선의 종류에 따라
     - 무방향 그래프(undirected graph)
       - (A, B) = (B, A)
     - 방향 그래프(directed graph)
       - <A, B> != <B, A>

   - 가중치 그래프, 네트워크 : 간선에 비용이나 가중치가 할당된 그래프

   - 부분 그래프

2. 용어

   - 인접 정점 : 간선에 의해 직접 연결된 정점

   - 차수(degree) : 정점에 연결된 간선의 수
     - 무방향 그래프
       - 차수의 합은 간선 수의 2배
     - 방향 그래프
       - 진입차수, 진출차수
       - 모든 진입(진출) 차수의 합은 간선의 수

   - 그래프의 경로
     - 무방향 그래프의 정점 s로부터 정점 e까지의 경로
       - 정점의 나열 s, v1, v2, ... , vk, e
       - 반드시 간선 (s, v1), (v1, v2), ... , (vk, e) 존재해야 함
     - 방향 그래프의 정점 s로부터 정점 e까지의 경로
       - 정점의 나열 s, v1, v2, ... , vk, e
       - 반드시 간선 <s, v1>, <v1, v2>, ... , <vk, e> 존재해야 함

   - 경로의 길이 : 경로를 구성하는데 사용된 간선의 수

   - 단순 경로 : 경로 중에서 반복되는 간선이 없는 경로

   - 사이클 : 시작 정점과 종료 정점이 동일한 경로

   - 연결 그래프 : 모든 정점들 사이에 경로가 존재하는 그래프

   - 트리 : 사이클을 가지지 않는 연결 그래프

   - 완전 그래프
     - 모든 정점 간에 간선이 존재하는 그래프
     - n개의 정점을 가진 무방향 완전그래프의 간선의 수 = n * (n-1) / 2

3. 그래프의 표현

   - 인접 행렬을 이용한 표현

     - 인접 행렬 M을 이용

     - 간선 (i, j)가 있으면, M\[i][j\] = 1, 또는 True

     - 그렇지 않으면, M\[i]\[j] = 0, 또는 False

     - 무방향 그래프 : 인접 행렬이 대칭

       ![image](https://user-images.githubusercontent.com/87686562/148943026-e82f52c5-f797-46bf-8301-d5a9fafc2e9a.png)

       ![image](https://user-images.githubusercontent.com/87686562/148943174-ae074983-919e-4750-80bb-5f6748e550dc.png)

       ![image](https://user-images.githubusercontent.com/87686562/148943261-7ba08f42-e03c-496f-98b9-7bd7153a951d.png)

4. 인접 행렬과 인접 리스트의 복잡도 비교

   | 인접 행렬                                                    | 인접 리스트                                                  |
   | ------------------------------------------------------------ | ------------------------------------------------------------ |
   | 간선의 수에 무관하게 항상 **<u>n^2개의 메모리 공간</u>**이 필요함<br />따라서 정점에 비해 간선의 수가 매우 많은 **<u>조밀 그래프에서 효과적</u>** | n개의 연결 리스트가 필요하고, 2e개의 노드가 필요함<br />즉 **<u>n + 2e개의 메모리 공간</u>**이 필요함<br />따라서 정점에 비해 간선의 개수가 매우 적은 **<u>희소그래프에서 효과적</u>** |
   | u와 v를 연결하는 간선의 유무는 M\[u][v]를 조사하면 알 수 있음<br />따라서 getEdge(u, v)의 시간 복잡도는 O(1)임 | getEdge(u, v)연산은 정점 u의 연결 리스트 전체를 조사해야 함<br />정점 u의 차수를 d_u라고 한다면 이 연산의 시간 복잡도는 O(d_u)임 |
   | 정점의 차수를 구하는 degree(v)는 정점 v에 해당하는 행을<br />조사하면 되므로 O(n)임. 즉, 정점 v에 대한 차수는 표 아래와 같이 계산됨 | 정점 v의 차수 degree(v)는 v의 연결 리스트의 길이를 반환하면 됨.<br />따라서 시간 복잡도는 O(d_v) |
   | 정점 v의 인접 정점을 구하는 adjacent(v)연산은<br />해당 행의 모든 요소를 검사하면 되므로 O(n)의 시간이 요구 | 정점 v에 간선으로 직접 연결된 모든 정점을 구하는 adjacent(v)도<br />해당 연결리스트의 모든 요소를 방문해야 되므로 O(d_v)임 |
   | 그래프에 존재하는 모든 간선의 수를 알아내려면<br />인접 행렬 전체를 조사해야 하므로 n^2번의 조사가 필요함.<br />따라서 O(n^2)의 시간이 요구됨 | 전체 간선의 수를 알아내려면 헤더 노드를 포함하여<br />모든 인접 리스트를 조사해야 하므로 O(n+e)의 연산이 요구됨 |

   - 정점 v에 대한 차수

     ![image](https://user-images.githubusercontent.com/87686562/149060620-9eef32b3-35f4-42e7-8b77-678374277fa6.png)
   
     

   

5. 인접 행렬 표현

   ![image](https://user-images.githubusercontent.com/87686562/148945294-50c5dd17-6863-4f2e-949b-897081173080.png)

   ![image](https://user-images.githubusercontent.com/87686562/148945368-1bb97f0d-ff57-42ae-92ab-97c9e19bf1b7.png)

6. 인접 리스트 표현

   ![image](https://user-images.githubusercontent.com/87686562/148945452-756935a9-5466-4711-8192-3783f17c3d93.png)

   ![image](https://user-images.githubusercontent.com/87686562/148945526-1dd76ab5-bb3a-4c65-b4f6-098f9f31c4d8.png)

---

## 그래프의 탐색이란?

- 가장 기본적인 연산
  - 시작 정점부터 차례대로 모든 정점들을 한 번씩 방문
  - 많은 문제들이 단순히 탐색만으로 해결
    - 도로망 예 : 특정 도시에서 다른 도시로 갈 수 있는지 여부
    - 전자회로 예 : 특정 단자와 다른 단자의 연결 여부

1. 방법

   - 깊이 우선 탐색 (DFS, Depth-First Search)

     - 한 방향으로 끝까지 가다가 더 이상 갈 수 없게 되면 가장 가까운 갈림길로 돌아와서 다른 방향으로 다시 탐색 진행

     - 되돌아가기 위해서는 스택 필요

       - 순환함수 호출로 묵시적인 스택 이용

     - 깊이 우선 탐색의 예

       <img src="https://user-images.githubusercontent.com/87686562/148946229-a2869d8a-a0e3-467d-9c09-1053f07b7ea4.png" alt="image" style="zoom: 80%;" />

     - 파이썬 구현 코드

       ```python
       def dfs(graph, start, visited = set()):		# visited : 공집합
           if start not in visited:		  # start가 방문하지 않은 정점이면
               visited.add(start)		  # start를 방문한 노드 집합에 추가
               print(start, end = ' ')		  # start를 방문했다고 출력
               nbr = graph[start] - visited		# nbr : 차집합 연산 이용
               for v in nbr:		  # v is an element {인접정점} - {방문정점}
                   dfs(graph, v, visited)		# v에 대해 dfs를 순환적으로 호출
       ```

   - 너비 우선 탐색 (BFS, Breadth-First Search)

     - 시작 정점으로부터 가까운 정점을 먼저 방문하고 멀리 떨어져 있는 정점을 나중에 방문하는 순회 방법
     
     - 큐를 사용하여 구현됨
     
     - 너비 우선 탐색의 예
     
       <img src="https://user-images.githubusercontent.com/87686562/148946835-31eddf8c-e93a-47b2-995e-2af00c4ec153.png" alt="image" style="zoom:80%;" />
     
     - 파이썬 구현 코드
     
       ```python
       import collections
       
       def bfs(graph, start):
           visited = set([start])		# 처음에는 start만 방문한 정점
           queue = collections.deque([start])		# 컬렉션의 덱 객체 생성(큐로 사용)
           while queue:		# 공백이 아닐 때까지
               vertex = queue.popleft()		# 큐에서 하나의 정점 vertex를 꺼냄
               print(vertex, end = ' ')		# vertex는 방문했음을 출력
               nbr = graph[vertex] - visited		# nbr : 차집합 연산 이용
               for v in nbr:		# v is an element {인접정점} - {방문정점}
                   visited.add(v)		# 이제 v는 방문했음
                   queue.appned(v)		# v를 큐에 삽입
       ```

2. 성능

   - DFS, BFS
     - 인접 행렬 표현 : O(n^2)
     - 인접 리스트로 표현 : O(n + e)
   - 완전 그래프와 같은 조밀 그래프 -> 인접 행렬이 유리
   - 희소 그래프 -> 인접 리스트가 유리

---

## 연결 성분 검사

### 연결 성분이란?

- 최대로 연결된 부분 그래프들을 구함

  - DFS 또는 BFS를 반복적으로 이용

    <img src="https://user-images.githubusercontent.com/87686562/148947490-2eaa8a33-f120-49b4-a62d-1430f5422f14.png" alt="image" style="zoom:80%;" />

  - 파이썬 구현 코드

    ```python
    def find_connected_component(graph):
        visited = set()				# 이미 방문한 정점 집합
        colorList = []				# 부분 그래프별 정점 리스트
        
        for vtx in graph:		# 그래프의 모든 정점들에 대해
            if vtx not in visited:		# 방문하지 않은 정점이 있다면
                color = dfs_cc(graph, [], vtx, visited)		# 새로운 컬러 리스트
                colorList.append(color)		# 새로운 리스트 추가
        
        print('그래프 연결성분 개수 = %d' % len(colorList))
        print(colorList)
        
    def dfs_cc(graph, color, vertex, visited):
        if vertex not in visited:			# 아직 칠해지지 않은 정점에 대해
            visited.add(vertex)				# 방문했음
            color.append(vertex)			# 같은 색의 정점 리스트에 추가
            nbr = graph[vertex] - visited		# nbr : 차집합 연산 이용
            for v in nbr:		# v is an element {인접정점} - {방문정점}
                dfs_cc(graph, color, v, visited)	# 순환 호출
    	return color			# 같은 색의 정점 리스트 반환
    ```

---

## 신장 트리

### 신장 트리란?

- 그래프 내의 모든 정점을 포함하는 트리

  - 사이클을 포함하면 안됨, 간선의 수 = n - 1

    <img src="https://user-images.githubusercontent.com/87686562/148949406-0353c2f7-62bb-4490-a9e1-88ca3d0c2b7e.png" alt="image" style="zoom: 80%;" />

  - 신장 트리 알고리즘
  
    ```python
    import collections
    
    def bfsST(graph, start):
        visited = set([start])				# 맨 처음 start만 방문한 정점
        queue = collections.deque([start])			# 컬렉션의 덱 생성(큐로 사용)
        while queue:						# 공백이 아닐 때까지
            v = queue.popleft()				# 큐에서 하나의 정점 v를 빼냄
            nbr = graph[v] - visited		# nbr = {v의 인접정점} - {방문정점}
            for u in nbr:					# 갈 수 잇는 모든 인접 정점에 대해
                print("(", v, ",", u, ")", end = "")		# (v, u) 간선 추가
                visited.add(u)				# u는 방문했음.
                queue.append(u)				# u를 큐에 삽입
    ```

---

## 위상 정렬

### 위상 정렬이란?

- 방향 그래프에 대해 정점들의 선행 순서를 위배하지 않으면서 모든 정점을 나열하는 것

  <img src="https://user-images.githubusercontent.com/87686562/148950189-0a3df677-5315-4003-9175-533f64052e2d.png" alt="image" style="zoom:80%;" />

- 위상 정렬 과정

  <img src="https://user-images.githubusercontent.com/87686562/148950338-3a7852d3-317f-4442-be0b-6c8388e22b84.png" alt="image" style="zoom:80%;" />

- 위상 정렬 알고리즘

  ```python
  def topological_sort_AM(vertex, graph):
      n = len(vertex)
      inDeg = [0] * n		# 정점의 진입차수 저장
      
      for i in range(n):
          for j in range(n):
              if graph[i][j] > 0:
                  inDeg[j] += 1		# 진입차수를 1 증가시킴
      
      vlist = []		# 진입차수가 0인 정점 리스트를 만듦
      for i in range(n):
          if inDeg[i] == 0:
              vlist.append(i)
              
      while len(vlist) > 0:		# 리스트가 공백이 아닐 때까지
          v = vlist.pop()		# 진입차수가 0인 정점을 하나 꺼냄
          print(vertex[v], end = ' ')
          for u in range(n):
              if v != u and graph[v][u] > 0:
                  inDeg[u] -= 1			# 연결된 정점의 진입차수 감소
                  if inDeg[u] == 0:		# 진입차수가 0이면
                      vlist.append(u)		# vlist에 추가
  ```

  
