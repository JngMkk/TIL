MAX_QSIZE = 10
# 파이썬의 queue모듈
# 큐와 스택 클래스를 제공
import queue
from CircularQueue import CircularQueue

Q = queue.Queue(maxsize = 20)
for i in range(1, 10):
    Q.put(i)    # 삽입
print('큐의 내용 : ', end = '')
for _ in range(1, 10):
    print(Q.get(), end = ' ')    # 삭제
print()

# 덱은 스택이나 큐보다는 입출력이 자유로운 자료구조.
# 덱을 스택이나 큐로 사용할 수 있다.
# 덱(deque)은 double-ended quque의 줄임말
# 전단과 후단에서 모두 삽입 / 삭제가 가능한 큐
# 원형 큐를 이용하여 덱 구현
class CircularDeque(CircularQueue):
    def __init__(self):
        super().__init__()
    def addRear(self, item):
        self.enqueue(item)
    def deleteFront(self):
        return self.dequeue()
    def getFront(self):
        return self.peek()
    def addFront(self, item):
        if not self.isFull():
            self.items[self.front] = item
            self.front = self.front - 1
            if self.front < 0:
                self.front = MAX_QSIZE - 1
    def deleteRear(self):
        if not self.isEmpty():
            item = self.items[self.rear]
            self.rear = self.rear - 1
            if self.rear < 0:
                self.rear = MAX_QSIZE - 1
            return item
    def getRear(self):
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