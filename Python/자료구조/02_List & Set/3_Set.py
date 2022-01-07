"""
집합이란?

- 원소의 중복을 허용하지 않음
- 원소들 사이에 순서가 없음
    > 선형 자료구조가 아님
- 다양한 방법으로 구현할 수 있음
    > 리스트, 비트 벡터, 트리, 해싱 구조 등

"""

# 리스트를 이용한 구현

class Set:
    def __init__(self):
        self.items = []
    def size(self):
        return len(self.items)
    def display(self, msg):
        print(msg, self.items)
    def contains(self, item):
        for i in range(len(self.items)):
            if self.items[i] == item:
                return True
        return False
    def insert(self, item):
        if item not in self.items:
            self.items.append(item)
    def delete(self, item):
        if item in self.items:
            self.items.remove(item)
    def union(self, setB):
        setC = Set()
        setC.items = list(self.items)
        for item in setB.items:
            if item not in self.items:
                setC.items.append(item)
        return setC
    def intersect(self, setB):
        setC = Set()
        for item in setB.items:
            if item in self.itmes:
                setC.items.append(item)
        return setC
    def difference(self, setB):
        setC = Set()
        for item in self.items:
            if item not in setB.items:
                setC.items.append(item)
        return setC

# 테스트
setA = Set()
setA.insert('휴대폰')
setA.insert('지갑')
setA.insert('손수건')
setA.display('Set A:')

setB = Set()
setB.insert('빗')
setB.insert('파이썬 자료구조')
setB.insert('야구공')
setB.insert('지갑')
setB.display('Set B:')
setB.insert('빗')
setA.delete('손수건')
setA.delete('발수건')
setA.display('Set A:')
setB.display('Set B:')

setA.union(setB).display('A U B:')
setA.intersect(setB).display('A ^ B:')
setA.difference(setB).display('A - B:')