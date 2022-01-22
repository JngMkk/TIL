class Entry:
    def __init__(self, key, value):
        self.key = key
        self.value = value
    def __str__(self):
        return str("%s : %s" % (self.key, self.value))

# 리스트를 이용해 순차 탐색 맵 구현
class SequentialMap:
    def __init__(self):
        self.table = []
    def size(self):
        return len(self.table)
    def display(self, msg):
        print(msg)
        for entry in self.table:
            print("  ", entry)
    def insert(self, key, value):
        self.table.append(Entry(key, value))
    def search(self, key):
        pos = sequential_search(self.table, key, 0, self.size() - 1)
        if pos is not None:
            return self.table[pos]
        else:
            return None
    def delete(self, key):
        for i in range(self.size()):
            if self.table[i].key == key:
                self.table.pop(i)
                return

def sequential_search(data, key, low, high):
        for i in range(low, high + 1):
            if data[i].key == key:
                return i
        return None


# 테스트
m = SequentialMap()
m.insert('data', '자료')
m.insert('game', '게임')
m.insert('structure', '구조')
m.display('나의 단어장 :')
print('탐색 : game --> ', m.search('game'))
m.delete('game')
m.display('나의 단어장 :')