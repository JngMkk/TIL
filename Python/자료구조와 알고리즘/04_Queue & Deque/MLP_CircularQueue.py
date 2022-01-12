# 함수
from typing import Deque


def isEmpty():
    global SIZE, queue, rear, front
    if front == rear:
        return True
    else:
        return False

def isFull():
    global SIZE, queue, rear, front
    if (rear+1) % SIZE == front:
        return True
    else:
        return False

def enQueue(data):
    global SIZE, queue, rear
    if isFull():
        print('Queue is Full')
        return
    rear = (rear+1) % SIZE
    queue[rear] = data

def deQueue():
    global SIZE, queue, rear, front
    if isEmpty():
        print('Queue is Empty')
        return None
    front = (front+1) % SIZE
    data = queue[front]
    queue[front] = None
    return data

def peek():
    global SIZE, queue, rear, front
    if isEmpty():
        print('Queue is Empty')
        return None
    return queue[(front+1) % SIZE]

# 전역
SIZE = 5
queue = [None] * SIZE
front = rear = 0

# 메인
enQueue('화사')
enQueue('솔라')
enQueue('문별')
enQueue('선미')
enQueue('유현')
print(queue)
print(deQueue())
print(deQueue())
print(queue)
enQueue('아이유')
enQueue('소현')
print(queue)
print(deQueue())