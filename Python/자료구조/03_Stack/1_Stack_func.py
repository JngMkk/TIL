# 스택은 가장 최근에 들어온 데이터가 가장 먼저 나감.
# 스택의 용도 : 되돌리기, 함수호출, 괄호 검사, 미로 탐색 등
# 리스트를 이용한 스택의 구현(함수 버전)
top = []
def isEmpty():
    return len(top) == 0        # True / False
def push(item):
    top.append(item)
def pop():
    if not isEmpty():           # 공백상태가 아니면
        return top.pop(-1)      # 리스트 맨 뒤에서 하나 꺼내고 반환
def peek():
    if not isEmpty():
        return top[-1]
def size():
    return len(top)
def clear():
    global top
    top = []

# 테스트
for i in range(1, 6):
    push(i)
print(' push 5회 : ', top)
print(' pop() --> ', pop())
print(' pop() --> ', pop())
print(' pop 2회 : ', top)
push('홍길동')
push('이순신')
print(' push+2회 : ', top)
print(' pop() --> ', pop())
print(' pop  1회 : ', top)