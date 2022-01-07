class Node:				                    
    def __init__ (self, elem, link=None):	
        self.data = elem 			        
        self.link = link

# 원형연결리스트의 응용 : 연결된 큐
# 용량 제한이 없고, 삽입/삭제가 모두 O(1)
# head(front)만 사용하는 것 보다 tail을 사용하는 것이
# front와 rear에 바로 접근할 수 있다는 점에서 효율적
# why? 원형연결리스트는 rear가 front를 가리키고,
# Queue는 삽입은 rear에서, 삭제는 front에서 이뤄지므로
class CircularLinkedQueue:
    def __init__(self):
        self.tail = None
    def isEmpty(self):
        return self.tail == None
    def clear(self):
        self.tail = None
    def peek(self):
        """ 가장 먼저 삽입된(front) 노드의 DATA 반환 """
        if not self.isEmpty():
            return self.tail.link.data
    def enqueue(self, item):
        """ 삽입 연산 """
        n = Node(item, None)
        if self.isEmpty():
            n.link = n
            self.tail = n
        else:
            n.link = self.tail.link
            self.tail.link = n
            self.tail = n
    def dequeue(self):
        """ 삭제 연산 """
        if not self.isEmpty():
            data = self.tail.link.data
            if self.tail.link == self.tail:     # Queue에 하나의 노드만 있는 경우
                self.tail = None
            else:
                self.tail.link = self.tail.link.link
            return data
    def size(self):
        if self.isEmpty():
            return 0
        else:
            count = 1
            n = self.tail.link
            while not n == self.tail:
                n = n.link
                count += 1
            return count
    def display(self, msg = 'CircularLinkedQueue: '):
        print(msg, end = '')
        if not self.isEmpty():
            n = self.tail.link
            while not n == self.tail:
                print(n.data, end = ' ')
                n = n.link
            print(n.data, end = ' ')
        print()


# 테스트
q = CircularLinkedQueue()
for i in range(8): 
    q.enqueue(i)		
q.display()			            	
for i in range(5): 
    q.dequeue()		
q.display()
for i in range(8,14): 
    q.enqueue(i)	
q.display()