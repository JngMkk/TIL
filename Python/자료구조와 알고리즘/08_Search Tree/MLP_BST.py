# 함수
class TNode:
    def __init__(self):
        self.left = None
        self.right = None
        self.data = None

# 전역
memory = []
root = None
nameArray = ['BlackPink', 'StayC', 'Aespa', 'ITZY', 'IVE', 'Twice']


# 메인
node = TNode()
node.data = nameArray[0]
root = node
memory.append(node)

for name in nameArray[1:]:
    node = TNode()
    node.data = name
    current = root
    if name < current.data:
        current.left = node
    elif name > current.data:
        current.right = node
    else:
        continue
    memory.append(node)
