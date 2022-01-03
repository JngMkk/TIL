# 큐 자료구조
"""

- 먼저 들어 온 데이터가 먼저 나가는 형식(선입선출)의 자료구조
- 큐는 입구와 출구가 모두 뚫려 있는 터널과 같은 형태로 시각화 할 수 있음
- 리스트 자료형으로도 구현할 수 있으나 시간복잡도가 더 높음
- 리스트는 원소를 꺼내고 난 후 위치 조정작업이 필요하므로.. O(n)

"""

# deque 라이브러리 사용
from collections import deque

queue = deque()

# 삭제 |출구| <= 삽입(5) - 삽입(2) - 삽입(3) - 삽입(7) - 삭제() - 삽입(1) - 삽입(4) - 삭제() |입구| <= 삽입
# 시간복잡도 O(1)
queue.append(5)     # <<<< 삽입
queue.append(2)
queue.append(3)
queue.append(7)
queue.popleft()     # <<<< 삭제, 5 삭제
queue.append(1)
queue.append(4)
queue.popleft()

print(queue)    # 먼저 들어온 순서대로 출력         deque([3, 7, 1, 4])
queue.reverse() # 역순으로 바꾸기
print(queue)    # 나중에 들어온 원소부터 출력       deque([4, 1, 7, 3])