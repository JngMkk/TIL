# 파일 생성
f = open('file1.txt', 'w')
f.close()

# 파일에 쓰기
f = open('file1.txt', 'w')
f.write('Hello World!\nBye World!')
f.close()

# 인코딩
f = open('file2.txt', 'w', encoding = 'utf-8')
f.write('안녕하세요')
f.close()

# 파일 읽기 read(), readlines(), readline() : 한줄씩 읽어오기
f = open('file1.txt', 'r')
# a = f.readline()        # 첫번째 라인 1개 읽기, while 문으로 끝까지
# a = f.readlines()       # 리스트로 받아오기 (줄바꿈 x) 한 행이 리스트의 요소가 됨
a = f.read()              # 전체 라인 읽기 (하나의 문자열로)
print(a)
print(type(a))
print(len(a))
f.close()

for ch in a:
    print(ch, end= '')
print()

f = open('file1.txt', 'r')
while True:
    a = f.readline()        # \n이 default로 적용
    if not a:
        break
    print(a, end = '')
print()
f.close()

f = open('file1.txt', 'r')
a = f.readlines()
for l in a:
    print(l, end='')
print()
f.close()

# for문으로 바로
f = open('file1.txt', 'r')
for l in f:
    print(l, end = '')
print()
f.close()