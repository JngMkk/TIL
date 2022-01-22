# 이진 검색
import random

# 함수
def binSearch(ary, fdata):
    pos = -1
    start = 0
    end = len(ary) - 1
    while start <= end:
        middle = (start+end) // 2
        if fdata == ary[middle]:
            return middle
        elif fdata > ary[middle]:
            start = middle + 1
        else:
            end = middle - 1
    return pos


# 전역
SIZE = 10
dataAry = [random.randint(1,100) for _ in range(SIZE)]
findData = dataAry[random.randint(0, SIZE-1)]
dataAry.sort()

# 메인
print('배열 :', dataAry)
positon = binSearch(dataAry, findData)
if positon == -1 :
    print(findData, '없어요 ㅠ')
else :
    print(findData, '가 ', positon, ' 에 있음')