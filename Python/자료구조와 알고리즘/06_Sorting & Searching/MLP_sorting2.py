# 선택정렬
import random

# 함수
def findMinIndex(array):
    minIdx = 0
    for i in range(1, len(array)):
        if array[minIdx] > array[i]:
            minIdx = i
    return minIdx

# 전역
before = [random.randint(100, 200) for _ in range(8)]
after = []

# 메인
print('정렬 전 :', before)
for _ in range(len(before)):
    minPos = findMinIndex(before)
    after.append(before[minPos])
    before.pop(minPos)

print('정렬 후 :', after)