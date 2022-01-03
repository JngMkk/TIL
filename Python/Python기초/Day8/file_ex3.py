# 회원명단 출력
def input_member(filename):
    with open(f'{filename}', 'w') as f:
        while True:
            tmp = input('멤버를 입력하세요. (종료는 q) : ')
            if tmp == 'q':
                print('저장이 완료되었습니다.')
                break
            f.write(tmp + '\n')

def output_member(filename):
    with open(f'{filename}', 'r') as f:
        print(f.read())

def main_input():
    global a
    a = input('저장 1, 출력 2, 종료 q : ')
    return a

if __name__ == '__main__':
    while True:
        main_input()
        if a == 'q':
            print('종료합니다.')
            break
        elif a == '1':
            input_name = input('멤버 명단을 저장할 파일명을 입력하세요. : ')
            input_member(input_name)
        elif a == '2':
            output_name = input('멤버 명단이 저장된 파일명을 입력하세요. : ')
            output_member(output_name)
        else:
            continue