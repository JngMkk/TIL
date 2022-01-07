"""
리스트란?

- 리스트는 가장 자유로운 선형 자료구조
    > 순서를 가짐
    > 항목들이 순서대로 나열되어 있고, 각 항목들은 위치를 가짐
    > Stack, Queue, Deque과 차이점 : 자료의 접근 위치

- 구현 방법
    > 배열 구조
        . 구현이 간단
        . 항목 접근이 O(1)
        . 삽입, 삭제시 오버헤드
        . 항목의 개수 제한
    > 연결된 구조
        . 구현이 복잡
        . 항목 접근이 O(n)
        . 삽입, 삭제가 효율적
        . 크기가 제한되지 않음

- 파이썬의 리스트는 동적 배열로 구현됨
    > 필요한 양보다 넉넉한 크기의 메모리 사용

- 파이썬 리스트의 시간 복잡도
    > append(a) 연산 : 대부분의 경우 O(1)   <- 배열 구조에서 맨 앞에 새로운 항목을 삽입하려먼 먼저 모든 항목을 한 칸씩 뒤로 이동시켜야 함
    > insert(pos, a) 연산 : O(n)           <- 배열 구조에서 맨 앞에서 항목을 삭제하면 이후의 모든 항목들을 한 칸씩 앞으로 이동시켜야 함
    > pop(pos) 연산 : O(n)

"""


# 배열로 구현한 리스트(함수 버전)
# 자료구조 리스트의 ADT 구현에 파이썬 리스트 이용
# 전역변수와 함수로 구현
items = []
def insert(pos, elem):
    items.insert(pos, elem)
def delete(pos):
    return items.pop(pos)
def getEntry(pos):
    return items[pos]
def isEmpty():
    return len(items) == 0
def size():
    return len(items)
def clear():
    global items
    items = []
def find(item):
    return items.index(item)
def replace(pos, elem):
    items[pos] = elem
def sort():
    items.sort()
def merge(lst):
    items.extend(lst)
def display(msg = 'ArrayList : '):
    print(msg, size(), items)

# # 테스트
# display('파이썬 리스트로 구현한 리스트 테스트')
# insert(0, 10); insert(0, 20); insert(1, 30); insert(size(), 40); insert(2, 50)
# display('파이썬 리스트로 구현한 List(삽입x5) : ')
# sort()
# display('파이썬 리스트로 구현한 List(정렬후) : ')
# replace(2, 90)
# display('파이썬 리스트로 구현한 List(교체후) : ')
# delete(2); delete(size() - 1)
# display('파이썬 리스트로 구현한 List(삭제후) : ')
# lst = [1, 2, 3]
# merge(lst)
# display('파이썬 리스트로 구현한 List(병합후) : ')
# clear()
# display('파이썬 리스트로 구현한 List(정리후) : ')


# 배열로 구현한 리스트(클래스 버전)
class ArrayList:
    def __init__(self):
        self.items = []
    def insert(self, pos, elem):
        self.items.insert(pos, elem)
    def delete(self, pos):
        return self.items.pop(pos)
    def isEmpty(self):
        return self.size() == 0
    def getEntry(self, pos):
        return self.items[pos]
    def size(self):
        return len(self.items)
    def clear(self):
        self.items = []
    def find(self, item):
        return self.items.index(item)
    def replace(self, pos, elem):
        self.items[pos] = elem
    def sort(self):
        self.items.sort()
    def merge(self, lst):
        self.items.extend(lst)
    def display(self, msg = 'ArrayList : '):
        print(msg, '항목 수 : ', self.size(), self.items)

# # 테스트
# s = ArrayList()
# s.display('파이썬 리스트로 구현한 리스트 테스트')
# s.insert(0, 10); s.insert(0, 20); s.insert(1, 30); s.insert(s.size(), 40); s.insert(2, 50)
# s.display("파이썬 리스트로 구현한 List(삽입x5): ")
# s.sort()
# s.display("파이썬 리스트로 구현한 List(정렬후): ")
# s.replace(2, 90)
# s.display("파이썬 리스트로 구현한 List(교체후): ")
# s.delete(2); s.delete(s.size() - 1)
# s.display("파이썬 리스트로 구현한 List(삭제후): ")
# lst = [1, 2, 3]
# s.merge(lst)
# s.display("파이썬 리스트로 구현한 List(병합후): ")
# s.clear()
# s.display("파이썬 리스트로 구현한 List(정리후): ")