"""
스택의 응용 : 미로 탐색

- 미로의 입구에서 시작해서 출구를 찾아 가는 문제
- 시행착오를 이용하는 탐색방법
    > 하나의 경로를 시도해 보고 막히면 다시 다른 경로를 시도
    > 가던 길이 막히면 가장 최근 갈림길로 돌아가서 다른 길을 찾음

- 깊이우선탐색(Depth-Frist Search) 알고리즘
    > 스택에 지나온 경로를 저장

"""
from Stack_class import Stack

# 미로 탐색 DFS
def isValidPos(x, y):
    """ (x, y)가 갈 수 있는 방인지 검사하는 함수 """

    if x < 0 or y < 0 or x >= MAZE_SIZE or y >= MAZE_SIZE:
        return False                                        # (x, y)가 미로 밖이면 갈 수 없음
    else:                                                   # 출구('x')이거나 방('0')이면 갈 수 있음
        return map[y][x] == '0' or map[y][x] == 'x'

def DFS():
    stack = Stack()
    stack.push((0, 1))                          # 시작위치 삽입(튜플)
    print('DFS : ')

    while not stack.isEmpty():                  # 공백이 아닐 동안
        here = stack.pop()                      # 항목을 꺼냄
        print(here, end = '->')
        (x, y) = here
        if map[y][x] == 'x':                    # 출구이면 탐색 성공. True 반환
            return True
        else:
            map[y][x] = '.'                     # 현재위치를 지나왔다고 . 표시

            """ 4방향의 이웃을 검사해 갈 수 있으면 스택에 삽입 """
            if isValidPos(x, y - 1):
                stack.push((x, y - 1))          # 상
            if isValidPos(x, y + 1):
                stack.push((x, y + 1))          # 하
            if isValidPos(x - 1, y):
                stack.push((x - 1, y))          # 좌
            if isValidPos(x + 1, y):
                stack.push((x + 1, y))          # 우
        print('현재 스택 : ', stack)
    return False                                # 탐색 실패. False 반환


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