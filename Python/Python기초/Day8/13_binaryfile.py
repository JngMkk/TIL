# 이진파일 : 글자가 아닌 비트 단위로 의미가 있는 파일
# ex) 그림파일, 음악파일, 동영상파일, 엑셀파일, 한글파일, 실행파일(.exe)
# 텍스트 파일 : 메모장으로 열고 내용이 보이는 파일

# 이진파일 읽기
# open('이진파일이름', 'rb')
# read(1) : 1 바이트씩 읽기

# 이진파일 쓰기
# open('이진파일이름', 'wb')
# write()

# 이진파일 C:/Temp/에 notepad.exe를 복사
f1 = open('C:/Windows/notepad.exe', 'rb')
f2 = open('C:/Temp/notepad.exe', 'wb')

while True:
    inStr = f1.read(1)
    if not inStr:       # NULL 이면 break 파일의 끝. 더이상 읽을 것이 없다.
        break
    f2.write(inStr)
f1.close()
f2.close()