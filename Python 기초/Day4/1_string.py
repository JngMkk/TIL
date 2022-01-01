# len()
s = 'programming'
print(len(s))

# count(str) : 문자열 내에 특정 문자 개수 반환 (method)
print(s.count('r'))
print(s.count('m'))
print(s.count('ing'))

# find(str, start, end) : 문자열 내에서 특정 문자가 존재하는지 여부와 인덱스 반환 (method)
s = 'Data crawling is fun'
print(s.find('is'))         # 찾으면 인덱스 반환
print(s.find('parsing'))    # 찾는 문자열이 없는 경우 -1 반환
print(s.find('is', 5, 10))

# index(str, start, end) : 문자열 내에서 특정문자열의 시작 위치를 반환
# 없으면 에러 반환
print(s.index('is'))
# print(s.index('parsing'))     # 에러 발생
# print(s.index('is', 5, 15))   # 에러 발생

# 테스트
cities = '인천 대구 대전 부산 울산 청주 춘천'
city = input('도시명 입력 : ')
tmp = cities.find(city)
if tmp == -1:
    print('해당 도시 없음')
else:
    print('해당 도시 있음')

# split() 리스트로 반환
birth = input('생년월일 입력(0000/00/00) : ')
tmp = birth.split('/')
print(f'당신은 {tmp[0]}년에 태어났고\n생일은 {tmp[1]}월 {tmp[2]}일 이군요.')

# join() : 각 문자 사이에 특정문자 삽입하여 결합
# inplace : default False
a = 'aa'
a = a.join('bbb')
print(a)

a = '-'
a = a.join('1234')
print(a)

a = '2000/01/01'
a = a.split('/')
a = '-'.join(a)
print(a)

# replace(찾는 문자열, 변경할 문자열)
# 찾는 문자열이 없는 경우 원래 문자열을 반환
# inplace : default False
s = 'Python programming'
s = s.replace('Python', 'Java')
print(s)

# 대소문자 변경
# upper() : 대문자
# lower() : 소문자
# capitalize() : 첫 문자를 대문자로 변경
# title() : 각 단어의 첫 문자를 대문자로 변경
# swapcase() : 대문자는 소문자로, 소문자는 대문자로 변경
s = 'python Programming'
print(s.upper())
print(s.lower())
print(s.capitalize())
print(s.swapcase())
print(s.title())

# strip() : 문자열 앞뒤의 공백을 제거
# lstrip() : 문자열의 왼쪽의 공백을 제거
# rstrip() : 문자열의 오른쪽의 공백을 제거
s = '  python  '
print(s.strip())
print(s.lstrip())
print(s.rstrip())

# isalpha() : 문자 여부 결과 반환(True, False)
# isdigit() : 숫자 여부 결과 반환
# isspace() : 하나의 문자에 대하여 공백 여부 반환
# isalnum() : 문자 또는 숫자인지 확인
# islower() : 소문자 여부
# isupper() : 대문자 여부
s = '내 이름은 jmkang 이고 나이는 28 입니다'
s = s.split()
for tmp in s:
    if tmp.isdigit():
        print('숫자군요')
    else:
        print('숫자가 아니에요')

# 입력된 문자열에서 알바벳, 숫자의 개수, 스페이스, 기타의 개수를 각각 계산
sen = input('문장을 입력하세요 : ')
al = 0
digit = 0
space = 0
etc = 0
for tmp in sen:
    if tmp.isalpha():
        al += 1
    elif tmp.isdigit():
        digit += 1
    elif tmp.isspace():
        space += 1
    else:
        etc += 1
print(f'알파벳 {al}개, 숫자 {digit}개, 공백{space}개, 기타 {etc}개')
