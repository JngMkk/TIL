"""

우선순위 큐의 응용 : 전략적인 미로 탐색

- 전략 : 출구의 위치를 알고 있다고 가정. 가능한 가까운 방향을 먼저 선택
- 큐에 저장되는 항목 : (x, y, -d) 형태의 튜플
    > 우선순위 -d : 거리가 가까울 수록 우선순위가 높도록 함

"""

import math
(ox, oy) = (5, 4)
def dist(x, y):
    (dx, dy) = (ox - x, oy - y)
    return math.sqrt(dx * dx + dy * dy)         # (x, y)와 (ox, oy)의 유클리디언 거리

class PriorityQueueMAZE:
    def __init__(self):
        self.items = []
    def isEmpty(self):
        return len(self.items) == 0
    def size(self):
        return len(self.items)
    def clear(self):
        self.items = []
    def findMaxIndex(self):
        if self.isEmpty():
            return None
        else:
            highest = 0
            for i in range(1, self.size()):
                if self.items[i][2] > self.items[highest][2]:
                    highest = i
            return highest
    def enqueue(self, item):
        self.items.append(item)
    def dequeue(self):
        highest = self.findMaxIndex()
        if highest is not None:
            return self.items.pop(highest)
    def peek(self):
        highest = self.findMaxIndex()
        if highest is not None:
            return self.items[highest]

def isValidPos(x, y):
    if x < 0 or y < 0 or x >= MAZE_SIZE or y >= MAZE_SIZE:
        return False
    else:
        return map[y][x] == '0' or map[y][x] == 'x'

def MySmartSearch():                                        # 최소거리 전략의 미로탐색
    q = PriorityQueueMAZE()                                 # 우선순위 큐 객체 생성
    q.enqueue((0, 1, -dist(0, 1)))                          # 튜플에 거리정보 추가
    print('PQueueMAZE : ')

    while not q.isEmpty():
        here = q.dequeue()                                  # 출구와 거리가 가장 가까운 것이 삭제
        print(here[0:2], end = '->')
        x, y, _ = here
        if map[y][x] == 'x':
            return True
        else:
            map[y][x] = '.'
            if isValidPos(x, y - 1):
                q.enqueue((x, y - 1, -dist(x, y - 1)))
            if isValidPos(x, y + 1):
                q.enqueue((x, y + 1, -dist(x, y + 1)))
            if isValidPos(x - 1, y):
                q.enqueue((x - 1, y, -dist(x - 1, y)))
            if isValidPos(x + 1, y):
                q.enqueue((x + 1, y, -dist(x + 1, y)))
        print('우선순위큐 : ', q.items)
    return False


# 테스트
map = [['1', '1', '1', '1', '1', '1'],
	['e', '0', '1', '0', '0', '1'],
	['1', '0', '0', '0', '1', '1'],
	['1', '0', '1', '0', '1', '1'],
	['1', '0', '1', '0', '0', 'x'],
	['1', '1', '1', '1', '1', '1']]
MAZE_SIZE = 6
if MySmartSearch() == True : print('미로탐색성공')