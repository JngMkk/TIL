# 순차 검색
import random

# 함수
def seqSearch(ary, fdata):
    pos = -1
    for i in range(len(ary)):
        if ary[i] == fdata:
            pos = i
            break
    return pos

# 전역
SIZE = 20
dataAry = [random.randint(1, 100) for _ in range(SIZE)]
findData = dataAry[random.randint(0, SIZE-1)]

# 메인
print('배열 :', dataAry)
pos = seqSearch(dataAry, findData)
if pos == -1:
    print(findData, 'No data')
else:
    print(findData, '가', pos, '에 있음')