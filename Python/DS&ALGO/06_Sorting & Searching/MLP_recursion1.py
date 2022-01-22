# 함수
def openBox():
    global count
    print('종이 상자 열기')
    count -= 1
    if count == 0:
        print('** 반지 넣기 **')
        return
    openBox()
    print('종이 상자 닫기')
    return

# 전역
count = 3

# 메인
openBox()