def printStep(arr, val):
    print(' Step %2d = ' % val, end = '')
    print(arr)

# 선택 정렬
# 시간 복잡도 : O(n^2)
# 입력 자료의 구성과 상관없이 자료 이동 횟수가 미리 결정
def selection_sort(data):
    """ 처리되지 않은 데이터 중 가장 작은 데이터를 선택해 맨 앞에 있는 데이터와 바꾸는 것 반복 """

    n = len(data)
    for i in range(n - 1):                              # 마지막 정렬은 할 필요 없으므로 n - 1
        least = i                                       # 가장 작은 원소 인덱스
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
print()

"""
삽입 정렬?

. 정렬되어 있는 부분에 새로운 데이터를 올바른 위치에 삽입하는 과정 반복

. 시간 복잡도
    > 최선의 경우 O(n) : 이미 정렬되어 있는 경우
        - 비교 : (n - 1)번
        - 이동 : 2(n - 1)번
    > 최악의 경우 O(n^2) : 역순으로 정렬되어 있는 경우
        - 비교 : n(n - 1) / 2 => O(n^2)
        - 이동 : (n(n - 1) / 2) + 2(n - 1) => O(n^2)
    - 평균의 경우 O(n^2)

. 특징
    > 많은 이동 필요 (데이터가 클 경우 불리)
    > 안정된 정렬 방법
    > 대부분 정렬되어 있으면 매우 효율적

"""

def insertion_sort(data):

    n = len(data)
    for i in range(1, n):
        key = data[i]
        j = i - 1                                       # j index => 정렬된 것 중 가장 큰 수
        while j >= 0 and data[j] > key:
            data[j + 1] = data[j]
            j -= 1
        data[j + 1] = key
        printStep(data, i)

# MLP
def insertion_sort_mlp(data):
    n = len(data)
    for i in range(1, n):
        for j in range(i, 0, -1):                       # 인덱스 i부터 1까지 1씩 감소
            if data[j] < data[j - 1]:                   # 한 칸씩 왼쪽으로 이동
                data[j], data[j - 1] = data[j - 1], data[j]
            else:
                break
        printStep(data, i)


# 테스트
myData = [5,3,8,4,9,1,6,2,7]
print("Original :", myData)
insertion_sort(myData)
print("Insertion :", myData)
print()
myData = [5,3,8,4,9,1,6,2,7]
insertion_sort_mlp(myData)
print("Insertion_mlp :", myData)
print()

"""
버블 정렬?

. 기본 전략
    > 인접한 2개의 값을 비교하여 순서대로 서로 교환
    > 비교-교환 과정을 리스트 전체에 수행(스캔)
        - 한번의 스캔이 완료되면 리스트 오른쪽 끝에 가장 큰 값이 위치함
    > 끝으로 이동한 값을 제외하고 다시 스캔 반복

. 시간복잡도
    > 비교 횟수
        - 입력 자료가 역순 정렬인 경우(최악) : n(n - 1) / 2 = O(n^2)
        - 입력 자료가 이미 정렬된 경우(최선) : 한 번의 스캔

"""

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

# 정렬 응용 : Set
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

