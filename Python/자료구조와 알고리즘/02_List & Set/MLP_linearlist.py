## 함수 선언부
def add_data(friend):
    katok.append(None)      # 빈칸 추가
    idx = len(katok) - 1
    katok[idx] = friend

def insert_data(pos, friend):
    # katok.append(None)
    # idx = len(katok) - 1
    # while idx > pos:
    #     katok[idx] = katok[idx-1]
    #     katok[idx-1] = None
    #     idx -= 1
    # katok[pos] = friend
    katok.append(None)
    idx = len(katok) - 1
    for i in range(idx, pos, -1):
        katok[i] = katok[i-1]
        katok[i-1] = None
    katok[pos] = friend

def delete_data(pos):
    katok[pos] = None
    idx = len(katok)
    for i in range(pos+1, idx, 1):
        katok[i-1] = katok[i]
        katok[i] = None
    del katok[idx-1]
        

## 전역 변수부
katok = []

## 메인 코드부
add_data('다현')
add_data('정연')
add_data('쯔위')
add_data('사나')
add_data('지효')
add_data('모모')
insert_data(3, '미나')
delete_data(4)
print(katok)