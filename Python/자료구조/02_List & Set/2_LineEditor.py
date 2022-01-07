# 배열로 구현한 리스트로 라인 편집기 구현
"""
i : 라인 삽입. 행 번호와 문자열을 입력하면 그 행에 한 라인 추가
d : 한 라인 삭제. 행 번호를 입력하면 그 행을 삭제
r : 한 라인 변경. 행 번호와 문자열을 입력하면 그 행의 내용을 변경
p : 현재 내용 출력. 현재 문서의 모든 내용을 라인 번호와 함께 출력
l : 파일 입력. 지정된 파일로부터 라인을 읽어 들임
s : 파일 출력. 지정된 파일로 편집 내용을 저장
"""

from ArrayList import ArrayList


def LineEditor():
    lst = ArrayList()
    while True:
        command = input('[메뉴선택] i-입력, d-삭제, r-변경, p-출력, l-파일읽기, s-저장, q-종료 : ')
        if command == 'i':
            pos = int(input('입력행 번호 : '))
            tmp = input('입력행 내용 : ')
            lst.insert(pos, tmp)
        elif command == 'd':
            pos = int(input('삭제행 번호 : '))
            lst.delete(pos)
        elif command == 'r':
            pos = int(input('변경행 번호 : '))
            tmp = input('변경행 내용 : ')
            lst.replace(pos, tmp)
        elif command == 'p':
            print('Line Editor')
            for line in range(lst.size()):
                print('[%2d]' % line, end = '')
                print(lst.getEntry(line))
            print()
        elif command == 'l':
            filename = input('읽을 파일명 : ')
            try:
                infile = open(filename, 'r')
                lines = infile.readlines()
                for line in lines:
                    lst.insert(lst.size(), line.rstrip('\n'))
                infile.close()
            except FileNotFoundError as e:
                print(e)
                continue
        elif command == 's':
            filename = input('저장할 파일명 : ')
            outfile = open(filename, 'w')
            for i in range(lst.size()):
                outfile.write(lst.getEntry(i) + '\n')
            outfile.close()
        elif command == 'q':
            return
        else:
            continue

# 테스트
LineEditor()