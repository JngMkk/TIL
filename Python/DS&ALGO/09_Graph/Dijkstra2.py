"""
전체 노드의 개수가 10000개가 넘는 경우

- 우선순위 큐 사용해 구현
    - 우선순위가 가장 높은 데이터를 가장 먼저 삭제
    - 대부분의 프로그래밍 언어에서 표준 라이브러리 형태로 지원
    - 우선순위 큐를 구현하기 위해 힙 사용
        - 우선순위 큐 구현 방식
            - 리스트는 삽입 O(1) 삭제 O(N)
            - 힙은 O(logN) 삭제 O(logN)

"""

import heapq

# 오름차순 힙 정렬(Heap Sort)
def heapsort(iter):
    h = []
    result = []
    for value in iter:                  # 모든 원소를 차례대로 힙에 삽입
        heapq.heappush(h, value)
    for _ in range(len(h)):             # 힙에 삽입된 모든 원소를 차례대로 꺼내어 담기
        result.append(heapq.heappop(h))
    return result

