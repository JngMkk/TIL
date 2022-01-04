# 탐색 알고리즘

# 순차 탐색 알고리즘
# 평균 비교 횟수 : (n + 1)/2
# 최악의 경우 : n
# 시간 복잡도 : O(n)
def sequential_search(data, key, low, high):
    for i in range(low, high + 1):
        if data[i].key == key:
            return i
    return None

# 이진 탐색 알고리즘
# 시간 복잡도 : O(logn)
# 재귀함수
def binary_search(data, key, low, high):
    if low <= high:
        middle = (low + high) // 2      # 정수 나눗셈(몫)
        if key == data[middle].key:
            return middle
        elif key < data[middle].key:
            return binary_search(data, key, low, middle - 1)
        else:
            return binary_search(data, key, middle + 1, high)
    return None

# 이진 탐색 알고리즘 반복 구조
def binary_search_iter(data, key, low, high):
    while low <= high:
        middle = (low + high) // 2
        if key == data[middle].key:
            return middle
        elif key < data[middle].key:
            high = middle - 1
        else:
            low = middle + 1
    return None