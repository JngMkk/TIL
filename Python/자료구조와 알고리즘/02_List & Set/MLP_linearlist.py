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
select = -1

## 메인 코드부
if __name__ == '__main__':
    while select != 4:
        select = int(input('선택하세요(1: 추가, 2: 삽입, 3: 삭제, 4: 종료) : '))

        if select == 1:
            data = input('추가할 데이터 : ')
            add_data(data)
            print(katok)
        elif select == 2:
            pos = int(input('삽입할 위치 : '))
            data = input('추가할 데이터 : ')
            insert_data(pos, data)
            print(katok)
        elif select == 3:
            pos = int(input('삭제할 위치 : '))
            delete_data(pos)
            print(katok)
        elif select == 4:
            print(katok)
            break
        else:
            print('1~4 중 하나를 입력하세요')
            continue
            