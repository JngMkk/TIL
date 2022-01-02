class Node:				                    
    def __init__ (self, elem, link=None):	
        self.data = elem 			        
        self.link = link

class LinkedList:
    def __init__(self):
        self.head = None
    def isEmpty(self):
        return self.head == None
    def clear(self):
        self.head = None
    def size(self):
        n = self.head
        count = 0
        while not n == None:
            n = n.link
            count += 1
        return count
    def display(self, msg = 'LinkedList:'):
        print(msg, end = '')
        n = self.head
        while not n == None:
            print(n.data, end = '')
            n = n.link
        print()
    def getNode(self, pos):
        """ pos번째 노드(DATA + Link) 반환 """
        if pos < 0:
            return None
        n = self.head
        while pos > 0 and n != None:
            n = n.link
            pos -= 1
        return n
    def getEntry(self, pos):
        """ pos번째 노드의 DATA 반환 """
        n = self.getNode(pos)
        if n == None:
            return None
        else:
            return n.data
    def replace(self, pos, elem):
        n = self.getNode(pos)
        if n != None: n.data = elem
    def find(self, data):
        """ 입력된 DATA가 저장된 노드 반환 """
        n = self.head
        while n != None:
            if n.data == data:
                return n
            n = n.link
        return n
    def insert(self, pos, elem):
        """ 삽입 연산 """
        before = self.getNode(pos - 1)
        if before == None:
            self.head = Node(elem, self.head)
        else:
            n = Node(elem, before.link)
            before.link = n
    def delete(self, pos):
        """ 삭제 연산 """
        before = self.getNode(pos - 1)
        if before == None:
            if self.head != None:
                self.head = self.head.link
        elif before.link != None:
            before.link = before.link.link

# 테스트
s = LinkedList()
s.display('단순연결리스트로 구현한 리스트(초기상태): ')
s.insert(0, 10)
s.insert(0, 20)
s.insert(1, 30)
s.insert(s.size(), 40)
s.insert(2, 50)
s.display('단순연결리스트로 구현한 리스트(삽입x5): ')
print('getNode : ', s.getNode(4))
print('getEntry : ', s.getEntry(4))
print('find : ', s.find(40))
s.replace(2, 90)
s.display('단순연결리스트로 구현한 리스트(교체x1): ')
s.delete(2); s.delete(s.size() - 1); s.delete(0)
s.display('단순연결리스트로 구현한 리스트(삭제x3): ')
s.clear()
s.display('단순연결리스트로 구현한 리스트(정리후): ')