from Stack_class import Stack

# 미로 탐색 DFS
def isValidPos(x, y):
    """ (x, y)가 갈 수 있는 방인지 검사하는 함수 """
    if x < 0 or y < 0 or x >= MAZE_SIZE or y >= MAZE_SIZE:
        return False
    else:
        return map[y][x] == '0' or map[y][x] == 'x'

def DFS():
    stack = Stack()
    stack.push((0, 1))
    print('DFS : ')

    while not stack.isEmpty():
        here = stack.pop()
        print(here, end = '->')
        (x, y) = here
        if map[y][x] == 'x':
            return True
        else:
            map[y][x] = '.'
            """ 4방향의 이웃을 검사해 갈 수 있으면 스택에 삽입 """
            if isValidPos(x, y - 1):
                stack.push((x, y - 1))
            if isValidPos(x, y + 1):
                stack.push((x, y + 1))
            if isValidPos(x - 1, y):
                stack.push((x - 1, y))
            if isValidPos(x + 1, y):
                stack.push((x + 1, y))
        print('현재 스택 : ', stack)
    return False


# 테스트
map = [ [ '1', '1', '1', '1', '1', '1' ],
	  [ 'e', '0', '0', '0', '0', '1' ],
	  [ '1', '0', '1', '0', '1', '1' ],
	  [ '1', '1', '1', '0', '0', 'x' ],
	  [ '1', '1', '1', '0', '1', '1' ],
	  [ '1', '1', '1', '1', '1', '1' ]]
MAZE_SIZE = 6
result = DFS()
if result:
    print(' --> 미로탐색 성공')
else:
    print(' --> 미로탐색 실패')