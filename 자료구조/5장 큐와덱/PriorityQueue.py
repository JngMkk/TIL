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
. 응용분야
  - 시뮬레이션, 네트워크 트래픽 제어, OS의 작업 스케쥴링 등 
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
    def findMaxIndex(self):
        if self.isEmpty():
            return None
        else:
            highest = 0
            for i in range(1, self.size()):
                if self.items[i] > self.items[highest]:
                    highest = i
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

# 시간 복잡도
"""
. 정렬되지 않은 리스트 사용
  - enqueue() : 대부분의 경우 O(1)
  - findMaxIndex() : O(n)
  - dequeue(), peek() : O(n)
. 정렬된 리스트 사용
  - enqueue() : O(n)
  - dequeue(), peek() : O(1)
. 힙 트리
  - enqueue(), dequeue() : O(logn)
  - peek() : O(1)
"""