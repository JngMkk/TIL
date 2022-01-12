from ArrayList_test import ArrayList

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