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
    while True:
        if name < current.data:
            if current.left is None:
                current.left = node
                break
            current = current.left
        elif name > current.data:
            if current.right is None:
                current.right = node
                break
            current = current.right
        else:
            break
    memory.append(node)

findData = 'StayC'
current = root
while True:
    if current.data == findData:
        print(findData, 'Find!')
        break
    elif current.data > findData:
        if current.left is None:
            print(findData, 'No Data')
            break
        current = current.left
    else:
        if current.right is None:
            print(findData, 'No data')
            break
        current = current.right