def printStep(arr, val):
    print(' Step %2d = ' % val, end = '')
    print(arr)

# 선택 정렬
def selection_sort(data):
    n = len(data)
    for i in range(n - 1):
        least = i
        for j in range(i + 1, n):
            if data[j] < data[least]:
                least = j
        data[i], data[least] = data[least], data[i]     # 위치 교환
        printStep(data, i + 1)

# 테스트
myData = [5,3,8,4,9,1,6,2,7]
print("Original :", myData)
selection_sort(myData)
print("Selection :", myData)

# 삽입 정렬
def insertion_sort(data):
    n = len(data)
    for i in range(1, n):
        key = data[i]
        j = i - 1       # j index => 정렬된 것 중 가장 큰 수
        while j >= 0 and data[j] > key:
            data[j + 1] = data[j]
            j -= 1
        data[j + 1] = key
        printStep(data, i)

# 테스트
myData = [5,3,8,4,9,1,6,2,7]
print("Original :", myData)
insertion_sort(myData)
print("Insertion :", myData)

# 버블 정렬
def bubble_sort(data):
    n = len(data)
    for i in range(n - 1, 0, -1):
        bChanged = False
        for j in range(i):
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]
                bChanged = True
        if not bChanged:
            break
        printStep(data, n - i)

# 테스트
myData = [5,3,8,4,9,1,6,2,7]
print("Original :", myData)
bubble_sort(myData)
print("Bubble :", myData)

# 집합 정렬
# 시간복잡도 O(n^2) -> O(n)
class Set:
    def __init__(self):
        self.items = []
    def size(self):
        return len(self.items)
    def insert(self, item):
        if item in self.items:
            return
        for i in range(len(self.items)):
            if item < self.items[i]:
                self.items.insert(i, item)      # 내장함수 insert
                return
        self.items.append(item)
    def __eq__(self, setB):
        """ 두 집합의 비교 연산(같은지) """
        if self.size() != setB.size():
            return False
        for i in range(len(self.items)):
            if self.items[i] != setB.items[i]:
                return False
        return True
    def union(self, setB):
        newset = Set()
        a = 0
        b = 0
        while a < len(self.items) and b < len(setB.items):
            valueA = self.items[a]
            valueB = self.items[b]
            if valueA < valueB:
                newset.items.append(valueA)
                a += 1
            elif valueA > valueB:
                newset.items.append(valueB)
                b += 1
            else:
                newset.items.append(valueA)
                a += 1
                b += 1
        while a < len(self.items):      # 남은 원소 추가
            newset.items.append(self.items[a])
            a += 1
        while b < len(setB.items):      # 남은 원소 추가
            newset.items.append(setB.items[b])
            b += 1
        return newset

