import random

# 함수
def findMinIndex(array):
    minIdx = 0
    for i in range(1, len(array)):
        if array[minIdx] > array[i]:
            minIdx = i
    return minIdx

# 전역
# testAry = [55, 88, 33, 77]
testAry = [random.randint(1, 100) for _ in range(20)]

# 메인
print(testAry)
minPos = findMinIndex(testAry)
print('최솟값 :', testAry[minPos])