# 정렬 응용 : 집합 다시 보기
# 항상 정렬된 순으로 저장
# 집합의 비교나 합집합, 차집합, 교집합 효율적 구현 가능
# 삽입연산은 더욱 복잡
class Set:
    def __init__(self):
        self.items = []

    def size(self):
        return len(self.items)

    def display(self, msg):
        print(msg, self.items)

    def contains(self, item):
        for i in range(len(self.items)):
            if self.items[i] == item:
                return True
        return False

    def insert(self, item):                         # 정렬된 상태를 유지하면서 item 삽입
        if item in self.items:
            return
        for idx in range(len(self.items)):          # 삽입할 idx 찾기
            if item < self.items[idx]:
                self.items.insert(idx, item)
                return
        self.items.append(item)                     # 제일 클 경우

    def delete(self, item):
        if item in self.items:
            self.items.remove(item)

    def __eq__(self, setB):                         # 두 집합이 같은가? 시간 복잡도 O(n^2) -> O(n)으로 개선
        if self.size() != setB.size():
            return False
        for idx in range(len(self.items)):
            if self.items[idx] != setB.items[idx]:
                return False
        return True

    def union(self, setB):
        """ 
        합집합 연산 방법 
        - 가장 작은 원소들부터 비교하여 더 작은 원소를 새로운 집합에 넣고 그 집합의 인덱스 증가시킴
        - 만약 두 집합의 현재 원소가 같으면 하나만 넣음. 인덱스는 모두 증가시킴
        - 한쪽 집합이 모두 처리되면 나머지 집합의 남은 모든 원소를 순서대로 새 집합에 넣음
        - 시간 복잡도 O(n^2) -> O(n)으로 개선
        """
        setC = Set()
        a = 0       # 집합 self의 원소에 대한 인덱스
        b = 0       # 집합 setB의 원소에 대한 인덱스
        while a < len(self.items) and b < len(setB.items):
            valueA = self.items[a]
            valueB = setB.items[b]
            if valueA < valueB:
                setC.items.append(valueA)
                a += 1
            elif valueA > valueB:
                setC.items.append(valueB)
                b += 1
            else:                                   # 중복되는 원소이면
                setC.items.append(valueA)           # 하나만 넣고 인덱스 둘다 증가
                a += 1
                b += 1
        while a < len(self.items):                  # self에 남은 원소를 모두 추가
            setC.items.append(self.items[a])
            a += 1
        while b < len(setB.items):                  # setB에 남은 원소를 모두 추가
            setC.items.append(setB.items[b])
            b += 1
        return setC

    def intersect(self, setB):
        setC = Set()
        for item in setB.items:
            if item in self.itmes:
                setC.items.append(item)
        return setC

    def difference(self, setB):
        setC = Set()
        for item in self.items:
            if item not in setB.items:
                setC.items.append(item)
        return setC
