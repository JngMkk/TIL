class Node:				                    
    def __init__ (self, elem, link=None):	
        self.data = elem 			        
        self.link = link

class Entry:
    def __init__(self, key, value):
        self.key = key
        self.value = value
    def __str__(self):
        return str("%s : %s" % (self.key, self.value))

# 체이닝을 이용한 해시 맵 구현
class HashChainMap:
    def __init__(self, M):
        self.table = [None] * M
        self.M = M
    def hashFn(self, key):
        """ 탐색키가 문자열인 경우 """
        sum = 0
        for c in key:
            sum = sum + ord(c)
        return sum % self.M
    def insert(self, key, value):
        idx = self.hashFn(key)
        self.table[idx] = Node(Entry(key, value), self.table[idx])      # 전단 삽입
    def search(self, key):
        idx = self.hashFn(key)
        node = self.table[idx]
        while node is not None:
            if node.data.key == key:
                return node.data
            node = node.link
        return None
    def delete(self, key):
        idx = self.hashFn(key)
        node = self.table[idx]
        before = None
        while node is not None:
            if node.data.key == key:
                if before == None:
                    self.table[idx] = node.link
                else:
                    before.link = node.link
                return
            before = node
            node = node.link
    def display(self, msg):
        print(msg)
        for idx in range(len(self.table)):
            node = self.table[idx]
            if node is not None:
                print("[%2d] -> " % idx, end = '')
                while node is not None:
                    print(node.data, end = ' -> ')
                    node = node.link
                print()


# 테스트
m = HashChainMap(13)
m.insert('data', '자료')
m.insert('game', '게임')
m.insert('structure', '구조')
m.insert('sequential search', '선형 탐색')
m.insert('binary search', '이진 탐색')
m.display('나의 단어장 :')
print('탐색 : game --> ', m.search('game'))
print('탐색 : over --> ', m.search('over'))
print('탐색 : data --> ', m.search('data'))
m.delete('game')
m.display('나의 단어장 :')