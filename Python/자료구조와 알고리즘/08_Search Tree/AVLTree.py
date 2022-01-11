"""
AVL트리란?

- 모든 노드에서 왼쪽 서브트리와 오른쪽 서브트리의 높이 차가 1을 넘지 않는 이진탐색트리
    > 즉, 모든 노드의 균형 인수는 0이나 +- 1이 되어야 함
    > 균형 인수 = 왼쪽 서브트리 높이 - 오른쪽 서브트리 높이

- 평균, 최선, 최악 시간복잡도 : O(logn)

- 탐색 연산 : 이진 탐색트리와 동일

- 삽입 연산
    > 삽입 위치에서 루트까지의 경로에 있는 조상 노드들의 균형 인수에 영향을 미침
    > 삽입 후에 불균형 상태로 변한 가장 가까운 조상 노드(균형 인수가 +-2가 된 가장 가까운 조상 노드)의
      서브 트리들에 대하여 다시 재균형
    > 삽입 노드부터 균형 인수가 +-2가 된 가장 가까운 조상 노드까지 회전

- 삽입과 삭제 시 균형 상태가 깨질 수 있음
    > 균형이 깨지는 4가지 경우 (LL, LR, RL, RR)

"""
from BinarySearchTree import BSTMap, BSTNode
from Tree import CircularQueue, count_node, count_leaf, calc_height


# LL 회전 방법
def rotateLL(A):
    B = A.left      # 시계방향 회전
    A.left = B.right
    B.right = A
    return B

# RR 회전 방법
def rotateRR(A):
    B = A.right     # 반시계방향 회전
    A.right = B.left
    B.left = A
    return B

# RL 회전 방법
def rotateRL(A):
    B = A.right
    A.right = rotateLL(B)
    return rotateRR(A)

# LR 회전 방법
def rotateLR(A):
    B = A.left
    A.left = rotateRR(B)
    return rotateLL(A)

# 균형 인수
def calc_height_diff(n):
    if n == None:
        return 0
    return calc_height(n.left) - calc_height(n.right)

# 재균형 함수
def rebalance(parent):
    hDiff = calc_height_diff(parent)
    if hDiff > 1:
        if calc_height_diff(parent.left) > 0:
            parent = rotateLL(parent)
        else:
            parent = rotateLR(parent)
    elif hDiff < -1:
        if calc_height_diff(parent.right) < 0:
            parent = rotateRR(parent)
        else:
            parent = rotateRL(parent)
    return parent

# 삽입 함수
def insert_avl(parent, node):
    if node.key < parent.key:
        if parent.left != None:
            parent.left = insert_avl(parent.left, node)
        else:
            parent.left = node
        return rebalance(parent)
    elif node.key > parent.key:
        if parent.right != None:
            parent.right = insert_avl(parent.right, node)
        else:
            parent.right = node
        return rebalance(parent)
    else:
        print('중복된 키 에러')

def levelorder(root):
    queue = CircularQueue()
    queue.enqueue(root)
    while not queue.isEmpty():
        n = queue.dequeue()
        if n is not None:
            print(n.key, end = ' ')
            queue.enqueue(n.left)
            queue.enqueue(n.right)

class AVLMap(BSTMap):		
    def __init__ (self):	
        super().__init__()	

    def insert(self, key, value=None):
        n = BSTNode(key, value)
        if self.isEmpty():
           self.root = n
        else:
           self.root = insert_avl(self.root, n)

    def display(self, msg = 'AVLMap :'):
        print(msg, end='')
        levelorder(self.root)
        print()


# 테스트
node = [7,8,9,2,1,5,3,6,4]
map = AVLMap()

for i in node :
    map.insert(i)
    map.display('AVL(%d): ' % i)

print(" 노드의 개수 : %d" % count_node(map.root))
print(" 단말의 개수 : %d" % count_leaf(map.root))
print(" 트리의 높이 : %d" % calc_height(map.root))

# 이진탐색트리와 AVL트리 비교
node = [0,1,2,3,4,5,6,7,8,9]
map = BSTMap()
for i in node:
    map.insert(i)
    map.display('BST(%d): ' % i)
print(" 노드의 개수 : %d" % count_node(map.root))
print(" 단말의 개수 : %d" % count_leaf(map.root))
print(" 트리의 높이 : %d" % calc_height(map.root))

node = [0,1,2,3,4,5,6,7,8,9]
map = AVLMap()
for i in node:
    map.insert(i)
    map.display('AVL(%d): ' % i)
print(" 노드의 개수 : %d" % count_node(map.root))
print(" 단말의 개수 : %d" % count_leaf(map.root))
print(" 트리의 높이 : %d" % calc_height(map.root))