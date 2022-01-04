from CircularQueue import CircularQueue
# 큐의 응용 : 너비우선탐색
# 출발점에서부터 인접한 위치들을 먼저 방문한 다음
# 방문한 위치들에 인접한 위치들을 순서대로 찾아 가는 방법
def isValidPos(x, y):
    if x < 0 or y < 0 or x >= MAZE_SIZE or y >= MAZE_SIZE:
        return False
    else:
        return map[y][x] == '0' or map[y][x] == 'x'

def BFS():
    q = CircularQueue()
    q.enqueue((0, 1))
    print('BFS : ')

    while not q.isEmpty():
        here = q.dequeue()
        print(here, end = '->')
        x, y = here
        if map[y][x] == 'x':
            return True
        else:
            map[y][x] = '.'
            if isValidPos(x, y - 1):
                q.enqueue((x, y - 1))
            if isValidPos(x, y + 1):
                q.enqueue((x, y + 1))
            if isValidPos(x - 1, y):
                q.enqueue((x - 1, y))
            if isValidPos(x + 1, y):
                q.enqueue((x + 1, y))
    return False

# 테스트
map = [['1', '1', '1', '1', '1', '1'],
	['e', '0', '1', '0', '0', '1'],
	['1', '0', '0', '0', '1', '1'],
	['1', '0', '1', '0', '1', '1'],
	['1', '0', '1', '0', '0', 'x'],
	['1', '1', '1', '1', '1', '1']]
MAZE_SIZE = 6
result = BFS()
if result:
    print(' --> 미로탐색 성공')
else:
    print(' --> 미로탐색 실패')