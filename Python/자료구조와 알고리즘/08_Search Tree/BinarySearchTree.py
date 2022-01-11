"""
탐색트리란?

- 탐색을 위한 트리 기반의 자료구조
- 이진탐색트리
    > 효율적인 탐색을 위한 이진트리 기반의 자료구조
    > 삽입, 삭제, 탐색 : O(logn)
    > 모든 노드는 유일한 키를 가짐
    > 왼쪽 서브트리의 키들은 루트의 키보다 작음
    > 오른쪽 서브트리의 키들은 루트의 키보다 큼
    > 왼쪽과 오른쪽 서브트리도 이진탐색트리
    > 성능
        . 탐색, 삽입, 삭제 연산의 시간은 트리의 높이에 비례

"""

# 이진탐색트리의 노드 구조
class BSTNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.left = None
        self.right = None

# 값을 이용한 탐색은 모든 노드를 검사해야 하므로 키를 이용해서 탐색
# 순환 구조
def search_bst(n, key):		
    if n == None:
        return None
    elif key == n.key:		        	
        return n
    elif key < n.key:			        
        return search_bst(n.left, key)	
    else:				                
        return search_bst(n.right, key)	

# 반복 구조
def search_bst_iter(n, key):
    while n != None:			        
        if key == n.key:		        
            return n
        elif key < n.key:		        
            n = n.left			        
        else:				            
            n = n.right			        
    return None					        

# 값을 이용한 탐색 : 모든 노드를 검사해야 함
def search_value_bst(n, value):
    if n == None: 
        return None
    elif value == n.value:					
        return n
    res = search_value_bst(n.left, value) 	
    if res is not None:					
       return res							
    else:									
       return search_value_bst(n.right, value)

# 최대 노드
def search_max_bst(n):	
    while n != None and n.right != None:
        n = n.right
    return n

# 최소 노드
def search_min_bst(n):	
    while n != None and n.left != None:
        n = n.left
    return n

# 삽입 연산
def insert_bst(r, n):
    if n.key < r.key:                           # 삽입할 노드의 키가 루트보다 작으면
        if r.left is None:		                # 루트의 왼쪽 자식이 없다면
           r.left = n			                # n은 루트의 왼쪽 자식이 됨
           return True
        else:			    	                # 루트의 왼쪽 자식이 있다면
           return insert_bst(r.left, n)	        
    elif n.key > r.key:	        	            # 삽입할 노드의 키가 루트보다 크면
        if r.right is None:	    	            # 루트의 오른쪽 자식이 없으면
           r.right = n		        	        # n은 루트의 오른쪽 자식이 됨
           return True
        else:			            	
           return insert_bst(r.right, n)
    else: 				                        # 키가 중복된다면 
        return False			                # 삽입하지 않음

# 삭제 연산
# 3가지 경우
# 삭제하려는 노드가 단말 노드일 경우
def delete_bst_case1(parent, node, root):
    if parent is None:                      # 삭제할 단말 노드가 루트이면	    
        root = None			                # 공백 트리가 됨
    else:
        if parent.left == node: 	        # 삭제할 노드가 부모의 왼쪽 자식이면
            parent.left = None		        # 부모의 왼쪽 링크를 None
        else:				                # 오른쪽 자식이면
            parent.right = None		        # 부모의 오른쪽 링크를 None
    return root			                    # root가 변경될 수도 있으므로 root 반환

# 삭제하려는 노드가 자식이 하나일 경우
def delete_bst_case2(parent, node, root):
    if node.left is not None:
        child = node.left
    else:						
        child = node.right		
    if node == root:			
        root = child			
    else:
        if node is parent.left: 	
            parent.left = child		
        else:			        	
            parent.right = child	
    return root	

# 자식이 두 개일 경우
def delete_bst_case3(parent, node, root):
    succp = node		                    # 후계자의 부모 노드    	
    succ = node.right		    	        # 후계자 노드
    while (succ.left != None):		        # 후계자와 부모노드 탐색
        succp = succ			
        succ = succ.left
    if (succp.left == succ):		        # 후계자가 왼쪽 자식이면
        succp.left = succ.right		        # 후계자의 오른쪽 자식을 후계자부모의 왼쪽에 연결
    else:			            	        # 후계자가 오른쪽 자식이면
        succp.right = succ.right	        # 후계자의 오른쪽 자식을 후계자부모의 오른쪽에 연결
    node.key = succ.key	    		        # 후계자의 키와 값을
    node.value= succ.value                  # 삭제할 노드에 복사
    return root		            	        # 일관성 유지

# 삭제 연산
def delete_bst(root, key):
    if root == None: 
        return None       		
    parent = None                       		
    node = root                         	    
    while node != None and node.key != key:	
        parent = node
        if key < node.key: 
            node = node.left
        else: 
            node = node.right
    if node == None:
        return None       		
    if node.left == None and node.right == None:
        root = delete_bst_case1 (parent, node, root)
    elif node.left==None or node.right==None:	
        root = delete_bst_case2 (parent, node, root)
    else:
        root = delete_bst_case3 (parent, node, root)


# 이진탐색트리를 이용한 맵 클래스
class BSTMap():     
    def __init__(self):
        self.root = None
    def isEmpty (self): 
        return self.root == None	
    def clear(self): 
        self.root = None		        
    def size(self): 
        return count_node(self.root)	

    def search(self, key):
        return search_bst(self.root, key)
    def searchValue(self, key):
        return search_value_bst(self.root, key)
    def findMax(self):
        return search_max_bst(self.root)
    def findMin(self):
        return search_min_bst(self.root)
    def insert(self, key, value=None):	
        n = BSTNode(key, value)		    
        if self.isEmpty() :		        
           self.root = n			    
        else :				            
           insert_bst(self.root, n)	    
    def delete(self, key):		    
        delete_bst (self.root, key)
    def display(self, msg = 'BSTMap :'):
        print(msg, end = '')
        inorder(self.root)
        print()

# # 테스트
# map = BSTMap()
# data = [35, 18,  7, 26, 12,  3, 68, 22, 30, 99]
# print("[삽입 연산] : ", data)
# for key in data :
#     map.insert(key)		                                
# map.display("[중위 순회] : ")
# if map.search(26) != None:
#     print('[탐색  26 ] : 성공')	
# else:
#     print('[탐색  26 ] : 실패')
# if map.search(25) != None:
#     print('[탐색  25 ] : 성공')	
# else:
#     print('[탐색  25 ] : 실패')
# map.delete(3); 	map.display("[   3 삭제] : ")	
# map.delete(68);	map.display("[  68 삭제] : ")	
# map.delete(18);	map.display("[  18 삭제] : ")	
# map.delete(35);	map.display("[  35 삭제] : ")	


# 중위 순회
# 정렬
def inorder(n):
    if n is not None:
        inorder(n.left)
        print(n.key, end = ' ')
        inorder(n.right)

# 연산
# 노드 개수
def count_node(n):
    if n is None:
        return 0
    else:
        return 1 + count_node(n.left) + count_node(n.right)     # 순환 이용