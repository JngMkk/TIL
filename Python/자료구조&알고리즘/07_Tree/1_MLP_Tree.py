# MLP 특강

"""
트리란?

. 트리는 가계도와 같은 계층적인 구조를 표현할 때 사용할 수 있는 자료구조
. 용어
    > 루트 노드 : 부모가 없는 최상위 노드
    > 단말 노드 : 자식이 없는 노드
    > 크기 : 트리에 포함된 모든 노드의 개수
    > 깊이 : 루트 노드부터의 거리
    > 깊이 : 루트 노드부터의 거리
    > 높이 : 깊이 중 최댓값
    > 차수 : 각 노드의 (자식 방향) 간선 개수
        - 기본적으로 트리의 크기가 N일 때, 전체 간선의 개수는 N - 1개

이진 탐색 트리란?

. 이진 탐색이 동작할 수 있도록 고안된 효율적인 탐색이 가능한 자료구조
. 이진 탐색 트리의 특징 : 왼쪽 자식 노드 < 부모 노드 < 오른쪽 자식 노드

트리의 순회

. 트리 자료구조에 포함된 노드를 특정한 방법으로 한 번씩 방문하는 방법
    > 트리의 정보를 시각적으로 확인할 수 있다.
. 대표적인 트리 순회 방법
    > 전위 순회 : 루트를 먼저 방문
    > 중위 순회 : 왼쪽 자식을 방문한 뒤에 루트 방문
    > 후위 순회 : 왼쪽 자식 방문 후 오른쪽 자식을 방문한 뒤에 루트 방문
    > ex)
                        A

                    B       C

                E      E F      G
        
        - 전위 순회 : A -> B -> D -> E -> C -> F -> G
        - 중위 순회 : D -> B -> E -> A -> F -> C -> G
        - 후위 순회 : D -> E -> B -> F -> G -> C -> A

"""

# 트리 순회 구현 예제
class Node:
    def __init__(self, data, left_node, right_node):
        self.data = data
        self.left_node = left_node
        self.right_node = right_node
    def __repr__(self):
        return f'{self.data}, {self.left_node}, {self.right_node}'

# 예시
#       A
#   B       C

n = int(input('입력할 노드의 수: '))                     # 3개
tree = {}                                               # Key와 Value 가짐


for _ in range(n):                                      # 노드 개수동안 반복
    data, left_node, right_node = input().split()       # 입력 예시 : A B C -> B None None -> C None None
    if left_node == 'None':                             # 왼쪽 노드가 'None'이면
        left_node = None                                # 왼쪽 자식 없다.
    if right_node == 'None':                            # 오른쪽 노드가 'None'이면
        right_node = None                               # 오른쪽 자식 없다.
    tree[data] = Node(data, left_node, right_node)      # {'A' : (A, B, C), 'B' : (B, None, None), 'C' : (C, None, None)}

# 전위 순회
def pre_order(node):
    print(node.data, end = ' ')                         # node의 data를 출력한다.
    if node.left_node != None:                          # 노드의 왼쪽 자식이 None이 아니면
        pre_order(tree[node.left_node])                 # 노드의 왼쪽 자식을 출력하고 순환
    if node.right_node != None:
        pre_order(tree[node.right_node])

# 중위 순회
def in_order(node):
    if node.left_node != None:                          # 루트 노드(A)는 왼쪽 자식(B)이 None이 아니므로
        in_order(tree[node.left_node])                  # 순환. B 노드는 왼쪽 자식이 None이므로
    print(node.data, end = ' ')                         # 'B' 출력
                                                        # 'B'노드는 오른쪽 자식도 None이므로 순환 끝.
                                                        # 첫 번째 if문 내부의 순환 끝났으므로 'A'도 출력
    if node.right_node != None:                         # 루트노드의 오른쪽 자식은 None이 아니므로 
        in_order(tree[node.right_node])                 # 순환. C 노드는 왼쪽 자식이 None이므로 'C' 출력
                                                        # C 노드는 오른쪽 자식도 None이므로 순환 끝. 중위 순회 끝.

# 후위 순회
# 중위 순회와 비슷하게 해석하면 됨
def post_order(node):
    if node.left_node != None:
        post_order(tree[node.left_node])
    if node.right_node != None:
        post_order(tree[node.right_node])
    print(node.data, end = ' ')

pre_order(tree['A'])                                    # A - B - C
print()
in_order(tree['A'])                                     # B - A - C
print()
post_order(tree['A'])                                   # B - C - A
print()