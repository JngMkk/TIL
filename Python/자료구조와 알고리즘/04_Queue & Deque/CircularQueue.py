MAX_QSIZE = 10  # 원형 큐의 크기

class CircularQueue:
    def __init__(self):
        self.front = 0                                      # 큐의 전단 위치
        self.rear = 0                                       # 큐의 후단 위치
        self.items = [None] * MAX_QSIZE                     # 항목 저장용 리스트 [None, None, ...]
    def isEmpty(self):
        return self.front == self.rear
    def isFull(self):
        return self.front == (self.rear + 1) % MAX_QSIZE
    def clear(self):
        self.front = self.rear
    def enqueue(self, item):
        if not self.isFull():                               # 포화상태가 아니면
            self.rear = (self.rear + 1) % MAX_QSIZE         # rear 회전
            self.items[self.rear] = item                    # rear 위치에 삽입
    def dequeue(self):
        if not self.isEmpty():                              # 공백상태가 아니면
            self.front = (self.front + 1) % MAX_QSIZE       # front 회전
            return self.items[self.front]                   # front 위치 항목 반환
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