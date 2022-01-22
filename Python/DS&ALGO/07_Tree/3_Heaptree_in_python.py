# 힙(Heap)의 특징

"""

- 힙은 완전 이진 트리 자료구조의 일종
    > 완전 이진 트리: 루트 노드부터 시작하여 왼쪽 자식 노드, 오른쪽 자식 노드 순서대로
                    데이터가 차례대로 삽입되는 트리를 의미

- 힙에서는 항상 루트 노드를 제거

- 최소 힙 ( 오름차순 정렬 )
    > 루트 노드가 가장 작은 값을 가짐
    > 따라서 값이 작은 데이터가 우선적으로 제거
    > 구성 함수 : Min-Heapify()
        - (상향식) 부모 노드로 거슬러 올라가며, 부모보다 자신의 값이 더 작은 경우에 위치를 교체
        - 새로운 원소가 삽입, 제거되었을 때 O(logn)의 시간 복잡도로 힙 성질을 유지할 수 있음
        - 원소를 제거할 대는 가장 마지막 노드가 루트 노드의 위치에 오도록 함
        - 이후 루트 노드에서부터 하향식으로(더 작은 자식 노드로) Heapify() 진행

                                   0
                                    

                  1                                 2

          3               4                5               6

      7       8       9       10      11       12      13      14

   15  16  17   18 19   20  21   22 23   24 25   26  27  28  29   30


- 최대 힙 ( 내림차순 정렬 )
    > 루트 노드가 가장 큰 값을 가짐
    > 따라서 값이 큰 데이터가 우선적으로 제거

"""
import sys
import heapq
# Python : 최소 힙 제공
input = sys.stdin.readline

def heapsort(iterable):     # List, Tuple
    h = []
    result = []
    # 모든 원소를 차례대로 힙에 삽입
    for value in iterable:
        heapq.heappush(h, value)
    # 힙에 삽입된 모든 원소를 차례대로 꺼내어 담기
    for _ in range(len(h)):
        result.append(heapq.heappop(h))
    return result

# Max heap : 데이터 넣을 때와 꺼낼 때 (-) 부호 붙혀서
def heapsort2(iterable):
    h = []
    result = []
    for value in iterable:
        heapq.heappush(h, -value)
    for _ in range(len(h)):
        result.append(-heapq.heappop(h))
    return result

# 테스트
result = heapsort([1, 3, 5, 7, 9, 2, 4, 6, 8, 0])
result2 = heapsort2([1, 3, 5, 7, 9, 2, 4, 6, 8, 0])
print(result)
print(result2)