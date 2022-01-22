"""
연결된 구조란?

- 연결된 구조는 흩어진 데이터를 링크로 연결해서 관리

- 특징
    > 용량이 고정되지 않음. 필요할 때마다 할당
    > 중간에 자료를 삽입하거나 삭제하는 것이 용이
    > n번째 항목에 접근하는데 O(n)의 시간이 걸림

- 구조
    > 노드
        . Data field
        . Link field (하나 이상)
    > 헤드 포인터
        . 노드를 가리키는 포인터

- 종류
    > 단순 연결 리스트
                                 Node1              Node2              Node3
        | head pointer | -> | Data | link | -> | Data | link | -> | Data | link |

    > 원형 연결 리스트
        . 마지막 노드의 링크가 첫번째 노드를 가리킴

                                 Node1              Node2              Node3              Node1
        | head pointer | -> | Data | link | -> | Data | link | -> | Data | link | -> | Data | link |

    > 이중 연결 리스트
        . prevlink는 이전 Node를 nextlink는 다음 Node를 가리킴

                                        Node1                             Node2                              Node3
        | head pointer | -> | prevlink | Data | nextlink | -> | prevlink | Data | nextlink | -> | prevlink | Data | nextlink |
                                |                                |                                  |
                    None <-------             <-------------------               <-------------------


"""

# Node클래스
class Node:				                    
    def __init__ (self, elem, link=None):	
        self.data = elem                    # Data Field	        
        self.link = link                    # Link Field

# 단순연결리스트 응용 : 연결 리스트
class LinkedList:
    def __init__(self):
        self.head = None                        # 초기상태 : 헤드 포인터가 아무것도 가리키지 않음
    def isEmpty(self):
        return self.head == None
    def clear(self):
        self.head = None
    def size(self):
        n = self.head                           # 헤드포인터가 가리키는 Node (즉, 위 그림에서 Node1)
        count = 0
        while not n == None:                    # 마지막 노드의 link 주소는 None이므로 None일 때까지 반복
            n = n.link                          # link를 따라 다음 노드로 이동
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
        """ pos번째 노드 반환 """
        if pos < 0:
            return None
        n = self.head
        while pos > 0 and n != None:            # pos번 반복문
            n = n.link                          # 다음 노드로 이동
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
        if n != None:
            n.data = elem
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
        if before == None:                          # 제일 앞에 삽입하는 경우
            self.head = Node(elem, self.head)       # 헤드포인터가 삽입하는 노드를 가리키게 해야함
        else:
            n = Node(elem, before.link)             # 이전 노드의 링크(삽입 노드의 다음 노드를 가리키는 링크)를 삽입 노드의 링크로 가져온 후
            before.link = n                         # 이전 노드의 링크가 삽입 노드를 가리키게 함
    def delete(self, pos):
        """ 삭제 연산 """
        before = self.getNode(pos - 1)
        if before == None:                          # 시작노드를 삭제하는 경우
            if self.head != None:                   # 공백리스트가 아니라면
                self.head = self.head.link          # 헤드포인터가 시작노드의 다음노드를 가리키게 함
        elif before.link != None:                   # 중간 이후
            before.link = before.link.link          # 삭제 노드 이전 노드의 링크만 바꿔주면
                                                    # 삭제 노드를 참조하는 변수가 없기때문에 객체는 자동 삭제됨(파이썬)



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