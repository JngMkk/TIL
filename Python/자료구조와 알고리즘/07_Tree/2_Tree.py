# 트리
# 계층적인 자료의 표현에 적합한 자료구조

"""

이진 트리란?

- 모든 노드가 2개의 서브 트리를 갖는 트리
    > 서브트리는 공집할일 수 있음
    > 이진트리는 순환적으로 정의됨
    > 이진트리의 서브 트리들은 모두 이진트리여야 함
    > 노드의 개수가 n개이면 간선의 개수는 (n - 1)개
    > 높이가 h이면 h<최소> ~ (2^h - 1)개<최대>의 노드를 가짐
    > n개 노드의 이진 트리 높이 : log_2(n+1) ~ n
        . n개의 노드를 일렬로 늘어놓으면 트리의 높이가 최대인 n이 됨
    

- 포화 이진 트리(full binary tree)
    > 트리의 각 레벨에 노드가 꽉 차있는 이진트리
                    A

                B       C

            E      E F      G

- 완전 이진 트리(complete binary tree)
    > 높이가 h일 때 레벨 1부터 h-1까지는 노드가 모두 채워짐
    > 마지막 레벨 h에서는 노드가 순서대로 채워짐
                    A

                B       C

            E      E  F     G

         H    I  J

"""

# 이진트리의 표현(링크 표현법)
class TNode:
    def __init__(self, data, left, right):
        self.data = data
        self.left = left
        self.right = right


# 이진트리의 연산
"""
순회

- 트리에 속하는 모든 노드를 한 번씩 방문하는 것
- 선형 자료구조는 순회가 단순
- 트리는 다양한 방법이 있음
- 전위 순회, 중위 순회, 후위 순회

"""

# 전위 순회(preorder traversal) : VTR
# 루트 -> 왼쪽 서브트리 -> 오른쪽 서브트리
# ex) 노드의 레벨 계산, 구조화된 문서 출력
def preorder(n):
    if n is not None:
        print(n.data, end = ' ')
        preorder(n.left)        # 왼쪽 서브트리
        preorder(n.right)       # 오른쪽 서브트리

# 중위 순회(inorder traversal) : LVR
# 왼쪽 서브트리 -> 루트 -> 오른쪽 서브트리
# ex) 정렬
def inorder(n):
    if n is not None:
        inorder(n.left)
        print(n.data, end = ' ')
        inorder(n.right)

# 후위 순회(postorder traversal) : LRV
# 왼쪽 서브트리 -> 오른쪽 서브트리 -> 루트
# ex) 폴더 용량 계산
def postorder(n):
    if n is not None:
        postorder(n.left)
        postorder(n.right)
        print(n.data, end = ' ')

# 레벨 순회
# 노드를 레벨 순으로 검사하는 순회
# 큐를 사용해 구현
# 순환을 사용하지 않음
def levelorder(root):
    queue = CircularQueue()                 # 큐 객체 초기화
    queue.enqueue(root)                     # 최초에 큐에는 루트 노드만 들어있음
    while not queue.isEmpty():              # 큐가 공백상태가 아닌 동안
        n = queue.dequeue()                 # 큐에서 맨 앞의 노드 n을 꺼냄
        if n is not None:
            print(n.data, end = ' ')        # 먼저 노드 정보를 출력
            queue.enqueue(n.left)           # n의 왼쪽 자식 노드를 큐에 삽입
            queue.enqueue(n.right)          # n의 오른쪽 자식 노드를 큐에 삽입

# 이진 트리 연산
# 노드 개수
def count_node(n):
    if n is None:                           # n이 None이면 공백 트리 -> 0 반환
        return 0
    else:
        return 1 + count_node(n.left) + count_node(n.right)     # 순환 이용. 좌우 서브트리의 노드수의 합+1을 반환 (루트까지)

# 단말 노드의 수
def count_leaf(n):
    if n is None:
        return 0
    elif n.left is None and n.right is None:                # 단말노드 -> 1 반환
        return 1
    else:                                                   # 비단말 노드 : 좌우 서브트리의 결과 합을 반환
        return count_leaf(n.left) + count_leaf(n.right)

# 트리의 높이
def calc_height(n):
    if n is None:
        return 0
    hLeft = calc_height(n.left)         # 왼쪽 트리의 높이
    hRight = calc_height(n.right)       # 오른쪽 트리의 높이
    if hLeft > hRight:                  # 더 높은 높이에 1을 더해 반환 (루트까지)
        return hLeft + 1
    else:
        return hRight + 1



# 테스트
d = TNode('D', None, None)
e = TNode('E', None, None)
b = TNode('B', d, e)
f = TNode('F', None, None)
c = TNode('C', f, None)
root = TNode('A', b, c)

print('\n In-order : ', end = '')
inorder(root)
print('\n Pre-order : ', end = '')
preorder(root)
print('\n Post-order : ', end = '')
postorder(root)
print('\n Level-order : ', end = '')
levelorder(root)
print()
print(' 노드의 개수 : %d개' % count_node(root))
print(' 단말의 개수 : %d개' % count_leaf(root))
print(' 트리의 높이 : %d' % calc_height(root))



MAX_QSIZE = 10				    
class CircularQueue:
    def __init__(self):		
        self.front = 0			
        self.rear = 0			
        self.items = [None] * MAX_QSIZE	

    def isEmpty(self): 
        return self.front == self.rear
    def isFull(self):
        return self.front == (self.rear + 1) % MAX_QSIZE
    def clear(self): 
        self.front = self.rear
    def enqueue(self, item):
        if not self.isFull():			            
            self.rear = (self.rear + 1) % MAX_QSIZE	
            self.items[self.rear] = item		    
    def dequeue(self):
        if not self.isEmpty():			            
            self.front = (self.front + 1) % MAX_QSIZE	
            return self.items[self.front]	        
    def peek(self):
        if not self.isEmpty():
            return self.items[(self.front + 1) % MAX_QSIZE]
    def size(self):
       return (self.rear - self.front + MAX_QSIZE) % MAX_QSIZE
    def display(self):
        out = []
        if self.front < self.rear :
            out = self.items[self.front + 1 : self.rear + 1]
        else:
            out = self.items[self.front + 1 : MAX_QSIZE] \
                + self.items[0 : self.rear + 1]		
        print("[f=%s,r=%d] ==> " % (self.front, self.rear), out)