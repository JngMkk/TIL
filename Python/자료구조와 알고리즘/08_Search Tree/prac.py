# 함수
class TNode:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

# 전역
memory = []
root = None
nameArray = ['BlackPink', 'StayC', 'Aespa', 'ITZY', 'IVE', 'Twice']

node = TNode(nameArray[0])
root = node
for name in nameArray[1:]:
    current = root
    node = TNode(name)
    while True:
        if name > current.data:
            if current.right is None:
                current.right = node
                break
            current = current.right
        elif name < current.data:
            if current.left is None:
                current.left = node
                break
            current = current.left
        else:
            break

findData = 'Aespa'
current = root
while True:
    if findData == current.data:
        print('Find!')
        break
    elif findData < current.data:
        if current.left is None:
            print('No data')
            break
        current = current.left
    else:
        if current.right is None:
            print('No data')
            break
        current = current.right
