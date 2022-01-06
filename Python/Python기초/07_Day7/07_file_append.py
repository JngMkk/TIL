# append() : 파일 끝에 추가
# a 모드

f = open('file1.txt', 'a')
appendtext = '\nThis is Python Programming'
f.write(appendtext)
f.close()

f = open('file1.txt', 'r')
print(f.read())
f.close()