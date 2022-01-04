"""
덱이란?

- 덱은 스택이나 큐보다는 입출력이 자유로운 자료구조
- 덱을 스택이나 큐로 사용할 수 있음
- 덱은 double-ended queue의 줄임말
    > 전단과 후단에서 모두 삽입, 삭제가 가능한 큐

"""

# 파이썬 제공 queue 모듈 사용
import queue

# 테스트
Q = queue.Queue(maxsize = 20)
for i in range(1, 10):
    Q.put(i)                        # 삽입
print('큐의 내용 : ', end = '')
for _ in range(1, 10):
    print(Q.get(), end = ' ')       # 삭제
print()


# 원형 큐를 이용한 구현
# 원형 큐에서 추가되는 연산 : delete_rear(), add_front(), get_rear()    전단, 후단 삽입, 삭제 가능해야 하므로
from CircularQueue import CircularQueue

MAX_QSIZE = 10
class CircularDeque(CircularQueue):                 # 상속
    def __init__(self):
        super().__init__()                          # 부모 클래스의 생성자 호출
    def addRear(self, item):
        self.enqueue(item)
    def deleteFront(self):
        return self.dequeue()
    def getFront(self):
        return self.peek()
    def addFront(self, item):
        if not self.isFull():
            self.items[self.front] = item
            self.front = self.front - 1             # 반시계 방향으로 회전
            if self.front < 0:
                self.front = MAX_QSIZE - 1
    def deleteRear(self):
        if not self.isEmpty():
            item = self.items[self.rear]
            self.rear = self.rear - 1
            if self.rear < 0:
                self.rear = MAX_QSIZE - 1
            return item
    def getRear(self):                              # 후단 peek
        return self.items[self.rear]

# 테스트
dq = CircularDeque()
for i in range(9):
    if i % 2 == 0:
        dq.addRear(i)
    else:
        dq.addFront(i)
dq.display()
for i in range(2):
    dq.deleteFront()
for i in range(3):
    dq.deleteRear()
dq.display()
for i in range(9, 14):
    dq.addFront(i)
dq.display()