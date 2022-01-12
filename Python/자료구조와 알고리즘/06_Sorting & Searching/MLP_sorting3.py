import random

# 함수
def selectionSort(ary):
    n = len(ary)
    for cy in range(n-1):
        minIdx = cy
        for i in range(cy+1, n):
            if ary[minIdx] > ary[i]:
                minIdx = i
        ary[cy], ary[minIdx] = ary[minIdx], ary[cy]

# 전역
lst = [random.randint(100, 200) for _ in range(8)]

# 메인
print('정렬 전 :', lst)
selectionSort(lst)
print('정렬 후 :', lst)