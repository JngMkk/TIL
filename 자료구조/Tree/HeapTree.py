# 힙 트리
"""
힙이란?

- '더미'와 모습이 비슷한 완전이진트리 기반의 자료구조
- 가장 큰(또는 작은) 값을 빠르게 찾아내도록 만들어진 자료 구조
- 최대 힙, 최소 힙
    > 최대 힙 : 부모 노드의 키 값이 자식 노드의 키 값보다 크거나 같은 완전이진트리
    > 최소 힙 : 부모 노드의 키 값이 자식 노드의 키 값보다 작거나 같은 완전이진트리

힙의 연산

- 삽입 연산
    > Upheap
        . 루트 노드까지의 경로에 따라 적절한 위치를 찾을 때까지
          부모 노드와 교환하면서 위로 올라감
        . 시간 복잡도 : <최악의 경우> O(logn)
        . 최악? 루트 노드까지 올라가야 하므로 트리의 높이에 해당하는 비교연산 및 이동 필요

- 삭제 연산
    > Downheap
        . 루트 노드 삭제 후, 마지막 노드를 루트로 올림
        . 루트 노드와 더 큰 자식 노드를 비교 후 자식이 더 크면 교환
        . 이 과정을 자식이 없거나 자식이 더 작을 때까지 반복
        . 시간 복잡도 : <최악의 경우> O(logn)

힙의 구현

- 힙은 보통 배열을 이용하여 구현
    > 완전이진트리 -> 각 노드에 번호를 붙임 -> 배열의 인덱스

- 부모노드와 자식노드의 관계
    > 왼쪽 자식의 인덱스 = 부모의 인덱스 * 2
    > 오른쪽 자식의 인덱스 = 부모의 인덱스 * 2 + 1
    > 부모의 인덱스 = 자식의 인덱스 / 2

"""

# 최대 힙의 구현
class MaxHeap:
    def __init__(self):
        self.heap = []
        self.heap.append(0)                     # 0번 항목은 사용하지 않음
    def size(self):
        return len(self.heap) - 1
    def isEmpty(self):
        return self.size() == 0
    def parent(self, i):                        # 부모노드 반환
        return self.heap[i // 2]
    def left(self, i):                          # 왼쪽 자식 반환
        return self.heap[i * 2]
    def right(self, i):                         # 오른쪽 자식 반환
        return self.heap[i * 2 + 1]
    def display(self, msg = '힙 트리 : '):
        print(msg, self.heap[1:])
    def insert(self, n):                        # 삽입 연산
        self.heap.append(n)                     # 맨 마지막 노드로 일단 삽입
        i = self.size()                         # 노드 n의 위치
        while i != 1 and n > self.parent(i):    # 부모보다 큰 동안 계속 Upheap
            self.heap[i] = self.parent(i)       # 부모를 끌어내림
            i = i // 2                          # i를 부모의 인덱스로 올림
        self.heap[i] = n                        # 마지막 위치에 n 삽입
    def delete(self):
        parent = 1
        child = 2
        if not self.isEmpty():
            hroot = self.heap[1]                                                        # 삭제할 루트를 복사해 둠
            last = self.heap[self.size()]                                               # 마지막 노드
            while child <= self.size():                                                 # 마지막 노드 이전까지
                # 만약 오른쪽 노드가 더 크면 child를 1 증가 (기본은 왼쪽 노드)
                if child < self.size() and self.left(parent) < self.right(parent):
                    child += 1
                if last >= self.heap[child]:
                    break
                self.heap[parent] = self.heap[child]
                parent = child
                child *= 2
            
            self.heap[parent] = last                # 맨 마지막 노드를 부모위치에 복사
            self.heap.pop(-1)                       # 맨 마지막 노드 삭제
            return hroot


# 테스트
heap = MaxHeap()
data = [2, 5, 4, 8, 9, 3, 7 ,3]
print('[ 삽입 연산 ] : ', data)
for elem in data:
    heap.insert(elem)
heap.display('[ 삽입 후 ] : ')
heap.delete()
heap.display('[ 삭제 후 ] : ')
heap.delete()
heap.display('[ 삭제 후 ] : ')