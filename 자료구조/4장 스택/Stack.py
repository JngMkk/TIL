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