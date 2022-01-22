"""
퀵 정렬

- 기준 데이터를 설정하고 그 기준보다 큰 데이터와 작은 데이터의 위치를 바꾸는 방법
- 일반적인 상황에서 가장 많이 사용되는 정렬 알고리즘 중 하나
- 병합 정렬과 더불어 대부분의 프로그래밍 언어의 정렬 라이브러리의 근간이 되는 알고리즘
- 가장 기본적인 퀵 정렬은 첫 번째 데이터를 기준 데이터(Pivot)로 설정

- 시간복잡도
    . 평균의 경우 : O(NlogN)
    . 최악의 경우 : O(n^2)

"""

def quick_sort(array, start, end):
    # 리스트가 하나 이하의 원소만을 담고 있다면 종료
    if start >= end:
        return
    pivot = start       # 피벗은 첫번째 원소
    left = start + 1
    right = end
    while left <= right:
        # 피벗보다 큰 데이터를 찾을 때까지 반복
        while left <= end and array[left] <= array[pivot]:
            left += 1
        # 피벗보다 작은 데이터를 찾을 때까지 반복
        while right > start and array[right] >= array[pivot]:
            right -= 1
        if left > right:        # 엇갈렸다면 작은 데이터와 피벗을 교체
            array[right], array[pivot] = array[pivot], array[right]
        else:                   # 엇갈리지 않았다면 작은 데이터와 큰 데이터를 교체
            array[left], array[right] = array[right], array[left]
    
    # 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬 수행
    quick_sort(array, start, right-1)
    quick_sort(array, right+1, end)

def quick_sort2(array):
    # 리스트가 하나 이하의 원소만을 담고 있다면 종료
    if len(array) <= 1:
        return array
    pivot = array[0]
    tail = array[1:]

    left_side = [x for x in tail if x <= pivot]     # 분할된 왼쪽 부분
    right_side = [x for x in tail if x > pivot]     # 분할된 오른쪽 부분

    # 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬 수행하고, 전체 리스트 반환
    return quick_sort2(left_side) + [pivot] + quick_sort2(right_side)


# 테스트
arr = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]
quick_sort(arr, 0, len(arr) - 1)
print(arr)
arr = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]
print(quick_sort2(arr))
