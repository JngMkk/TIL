# 우선순위 큐
"""

. 실생활에서의 우선순위 - 도로에서의 자동차 우선순위

. 우선순위 큐
  - 우선순위 개념을 큐에 도입한 자료구조
  - 모든 데이터가 우선순위를 가짐
  - 입력 순서와 상관없이 우선순위가 높은 데이터가 먼저 출력
  - 가장 일반적인 큐로 볼 수 있다.
  - 우선순위를 어떻게 정하느냐에 따라 스택이나 큐로도 사용 가능
    > 빨리 들어온 항목에 더 높은 우선순위 : 큐
    > 빨리 들어온 항목에 더 낮은 우선순위 : 스택
  - 리스트를 이용해 구현할 수 있음
    > 삽입 시간 : O(1)
    > 삭제 시간 : O(n) => 데이터 찾는 시간
  - 힙(Heap)을 이용해 구현할 수 있음
    > 삽입 시간 : O(logn)
    > 삭제 시간 : O(logn)
  - 단순히 n개의 데이터를 힙에 넣었다가 모두 꺼내는 작업은 정렬과 동일(힙 정렬)
    > 시간복잡도 : O(nlogn)
  - 구현 방법
    > 배열 구조, 연결된 구조, 힙 트리
    
. 응용분야
  - 허프만 코딩 트리 : 빈도가 작은 두 노드 선택
  - Kruska MST 알고리즘 : MST에 포함되지 않은 간선 중에 최소가중치 간선 선택
  - Dijkstra의 최단거리 알고리즘 : 최단거리가 찾아지지 않은 정점들 중에서 가장 거리가 가까운 정점 선택
  - 인공지능 A* 알고리즘 : 상태 공간트리에서 가장 가능성이 높은 경로를 먼저 선택하여 시도
  - 시뮬레이션, 네트워크 트래픽 제어, OS의 작업 스케쥴링 등

. 시간복잡도
  - 정렬되지 않은 리스트 사용
    > enqueue() : 대부분의 경우 O(1)
    > findMaxIndex() : O(n)
    > dequeue(), peek() : O(n)
  - 정렬된 리스트 사용(순서가 있으므로 데이터들과 비교해야 함)
    > enqueue() : O(n)
    > dequeue(), peek() : O(1)
  - 힙 트리
    > enqueue(), dequeue() : O(logn)
    > peek() : O(1)

"""

# 정렬되지 않은 배열을 이용한 우선순위 큐의 구현
# Python List를 이용한 우선순위 큐 ADT 구현
class PriorityQueue:
    def __init__(self):
        self.items = []
    def isEmpty(self):
        return len(self.items) == 0
    def size(self):
        return len(self.items)
    def clear(self):
        self.items = []
    def findMaxIndex(self):                                 # 최대 우선순위 항목의 인덱스 반환
        if self.isEmpty():
            return None
        else:
            highest = 0                                     # 0을 최대라고 가정
            for i in range(1, self.size()):                 # 모든 항목에 대해 검사
                if self.items[i] > self.items[highest]:
                    highest = i                             # 최대보다 큰 값으로 갱신
            return highest
    def enqueue(self, item):
        self.items.append(item)
    def dequeue(self):
        highest = self.findMaxIndex()
        if highest is not None:
            return self.items.pop(highest)
    def peek(self):
        highest = self.findMaxIndex()
        if highest is not None:
            return self.items[highest]


# 테스트
q = PriorityQueue()
q.enqueue(34); q.enqueue(18); q.enqueue(27); q.enqueue(45); q.enqueue(15)
print('PQueue : ', q.items)
while not q.isEmpty():
    print('Max Priority = ', q.dequeue())
