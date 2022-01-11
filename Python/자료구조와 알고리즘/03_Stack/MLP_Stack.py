# 함수
def isFull():
    """ 스택이 꽉 찼는가? """
    if top >= SIZE - 1:
        return True
    return False

def push(data):
    global top
    if isFull():
        print('Stack is Full')
        return None
    top += 1
    stack[top] = data

def isEmpty():
    global top
    if top == -1:
        return True
    return False

def pop():
    global top
    if isEmpty():
        print('Stack is Empty')
        return None
    data = stack[top]
    stack[top] = None
    top -= 1
    return data

def peek():
    global top
    if isEmpty():
        print('Stack is Empty')
        return None
    return stack[top]

# 전역
SIZE = 5
# stack = [None for _ in range(SIZE)]
stack = [None] * SIZE
top = -1

# 메인
push('커피1')
push('커피2')
print(peek())
print(isFull())
retdata = pop()
print('pop :', retdata)
retdata = pop()
print('pop :', retdata)
retdata = pop()
print('pop :', retdata)
print(isEmpty())