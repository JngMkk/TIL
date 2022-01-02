# 큐는 선입선출의 자료구조이다.
# 삽입은 큐의 후단에서, 삭제는 전단에서 이루어진다.
# 프린터와 컴퓨터 사이의 인쇄 작업 큐
# 실시간 비디오 스트리밍에서의 버퍼링
# 시뮬레이션의 대기열
# 통신에서의 데이터 패킷들의 모델링에 이용
# 원형 큐가 훨씬 효율적
# 선형큐는 삽입 연산 : O(1) / 삭제 연산 : O(n)
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
        if self.front < self.rear:
            out = self.items[self.front + 1 : self.rear + 1]
        else:
            out = self.items[self.front + 1 : MAX_QSIZE] \
                + self.items[0 : self.rear + 1]
        print('[f = %s, r = %d] --> ' % (self.front, self.rear), out)

# # 테스트
# q = CircularQueue()
# for i in range(8):
#     q.enqueue(i)
# q.display()
# for i in range(5):
#     q.dequeue()
# q.display()
# for i in range(8,14): q.enqueue(i)
# q.display()