# 노드 클래스
class Node:
    def __init__(self, elem, link = None):      # 생성자. 디폴트 인수 사용
        self.data = elem                        # 데이터 멤버 생성 및 초기화
        self.link = link                        # 링크 생성 및 초기화

# 단순연결리스트 응용 : 연결된 스택(Linked Stack)
class LinkedStack:
    def __init__(self):
        self.top = None
    
    def isEmpty(self):
        """ 공백상태 검사 """
        return self.top == None
    def clear(self):
        """ 스택 초기화 """
        self.top = None
    def push(self, item):
        """ 삽입 연산 """
        n = Node(item, self.top)    # 노드 n의 링크가 시작노드를 가리키게 함
        self.top = n                # top이 n을 가리키도록 함
    def pop(self):
        """ 삭제 연산 """
        if not self.isEmpty():
            n = self.top            # 변수 n이 시작노드를 가리키도록 함
            self.top = n.link       # top이 다음노드를 가리키도록 함
            return n.data           # n이 가리키는 노드의 데이터를 반환함
    def size(self):
        """ 스택의 항목 수 연산 """
        n = self.top                # 시작 노드
        count = 0
        while not n == None:        # n이 None이 아닐 때 까지
            n = n.link              # 다음 노드로 이동
            count += 1
        return count
    def peek( self ):
        """ STACK에 가장 마지막에 들어간 DATA"""	
        if not self.isEmpty():	
            return self.top.data
    def display(self, msg='LinkedStack:'):
        print(msg, end='')		
        node = self.top			
        while not node == None :	 	
            print(node.data, end=' ')	
            node = node.link		    
        print()



# 테스트
odd = LinkedStack()		
even = LinkedStack()	
for i in range(10):		    	    
    if i%2 == 0 : even.push(i) 		
    else : odd.push(i)			    

even.display('스택 even push 5회: ')
odd.display ('스택 odd push 5회: ')
print('스택 odd size:', odd.size())	
print('스택 even peek: ', even.peek())
print('스택 odd peek: ', odd.peek())	
for _ in range(2) : even.pop()		
for _ in range(3) : odd.pop()		
even.display('스택 even pop 2회: ')
odd.display ('스택 odd pop 3회: ')