# 함수
class Node():
    def __init__(self):
        self.data = None
        self.link = None

def printNodes(start):
    current = start
    print(current.data, end = ' ')
    while current.link != None:
        current = current.link
        print(current.data, end = ' ')
    print()

def insert(findData, insertData):
    global memory, head, current, pre
    node = Node()
    node.data = insertData
    # 첫 노드 앞에 삽입
    if findData == head.data:
        node.link = head
        head = node
        memory.append(node)
        return
    # 중간에 삽입
    current = head
    while current.link != None:
        pre = current
        current = current.link
        if current.data == findData:
            pre.link = node
            node.link = current
            memory.append(node)
            return
    # 마지막에 삽입
    current.link = node
    memory.append(node)
    return

def delete(deleteData):
    global memory, head, current, pre
    # 첫 노드 삭제
    if deleteData == head.data:
        memory.remove(current)
        current = head
        head = head.link
        return
    # 두 번째 이후 삭제
    current = head
    while current.link != None:
        pre = current
        current = current.link
        if current.data == deleteData:
            memory.remove(current)
            pre.link = current.link
            return

def findNode(findData):
    global memory, head, current, pre
    current = head
    if current.data == findData:
        return current              # Node를 통째로 return
    while current.link != None:
        current = current.link
        if current == findData:
            return current
    return Node()

# 전역
memory = []     # c 언어.... Python은 없어도 됨
head, current, pre = None, None, None
dataArray = ['다현', '정연', '쯔위', '사나', '지효']

# 메인
node = Node()
node.data = dataArray[0]
head = node
memory.append(node)
for data in dataArray[1:]:
    pre = node
    node = Node()
    node.data = data
    pre.link = node
    memory.append(node)

insert('다현', '유현')
printNodes(head)

insert('사나', '세경')
printNodes(head)

insert('바보', '소현')
printNodes(head)

delete('유현')
printNodes(head)

delete('쯔위')
printNodes(head)

fNode = findNode('쯔위')
print(fNode.data)