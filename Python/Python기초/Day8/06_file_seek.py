# 파일 내에서 검색
# seek(offset, whence):
#   - offset : 상대위치 (시작 위치로부터 열의 위치)
#   - whence : 위치 (0 : 파일시작위치, 1 : 현재위치, 2 : 파일의 끝)

# seek(0, 0) : 시작위치로부터 0열의 위치 -> 0행 0열
# seek(10, 0) : 시작위치로부터 오른쪽으로 10열의 위치 -> 0행 10열
# seek(0, 2) : 파일의 끝으로부터 0열의 위치
f = open('file1.txt', 'r')
f.seek(15, 0)                # ['ye World!']
                             # 한글은 2 바이트씩
                             # enter키 입력하면 \r : carriage return \n : line feed가 자동으로 입력됨. 문자 수에 포함됨
lines = f.readlines()
print(lines)
f.close()

# read() 함수 사용
f = open('file1.txt', 'r')
a = f.read()
v = input('검색 값 입력 : ')        # 대/소문자 구분
if v in a:
    print('Exist')
else:
    print('None')