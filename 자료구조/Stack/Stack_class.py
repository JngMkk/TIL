"""
스택이란?

- 먼저 들어 온 데이터가 나중에 나가는 형식(선입후출)의 자료구조이다.
- 입구와 출구가 동일한 형태로 스택을 시각화할 수 있음.
- 파이썬 제공 리스트로도 구현할 수 있음 (append, pop)
- print(stack[::-1])    # 최상단 원소부터 출력 1 3 2 5 -> 제일 나중에 들어온 것이 가장 빨리 나가야 하므로
- print(stack)          # 최하단 원소부터 출력 5 2 3 1

"""

# 스택의 구현(클래스 버전)
class Stack:
    def __init__(self):
        self.top = []
    def isEmpty(self):
        return len(self.top) == 0
    def size(self):
        return len(self.top)
    def push(self, item):
        self.top.append(item)
    def pop(self):
        if not self.isEmpty():
            return self.top.pop(-1)
    def peek(self):
        if not self.isEmpty():
            return self.top[-1]
    def __str__(self):
        return str(self.top[::-1])  # 처음부터 끝까지 역순으로 나타내어라.

# # 테스트
# odd = Stack()
# even = Stack()
# for i in range(10):
#     if i % 2 == 0:
#         even.push(i)
#     else:
#         odd.push(i)
# print(' 스택 even push 5회: ', even)
# print(' 스택 odd  push 5회: ', odd)
# print(' 스택 even     peek: ', even.peek())
# print(' 스택 odd      peek: ', odd.peek())
# for _ in range(2):
#     even.pop()
# for _ in range(3):
#     odd.pop()
# print(' 스택 even  pop 2회: ', even)
# print(' 스택 odd   pop 3회: ', odd)