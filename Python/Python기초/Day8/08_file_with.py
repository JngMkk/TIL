# with문
# with문이 종료되면 파일객체는 자동으로 close()
# with open(file, 열기모드) as 파일객체:
#       수행코드

with open('file3.txt', 'w') as f:
    f.write('Hello World!\nThis is Python Programming\nOK! Bye World!')