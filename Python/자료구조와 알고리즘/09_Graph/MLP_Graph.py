# 함수
class Graph:
    def __init__(self, size):           # size : 정점의 개수
        self.size = size
        self.graph = [[0 for _ in range(size)] for _ in range(size)]

# 전역
G = None

# 메인
G = Graph(4)
G.graph[0][1] = 1
G.graph[0][2] = 1
G.graph[0][3] = 1
G.graph[1][0] = 1
G.graph[1][2] = 1
G.graph[2][0] = 1
G.graph[2][1] = 1
G.graph[2][3] = 1
G.graph[3][0] = 1
G.graph[3][2] = 1

for row in range(4):
    for col in range(4):
        print(G.graph[row][col], end = ' ')
    print()