pw = int(input('비밀번호 입력 : '))
if pw == 1234:
    print('비밀번호가 일치합니다.')
else:
    print('비밀번호가 일치하지 않습니다.')

id = input('아이디 입력 : ')
pw = input('비밀번호 입력 : ')
if id == 'multicampus' and pw == '1234':
    print('로그인 성공')
else:
    print('로그인 실패')

# 중첩 if문
if id == 'multicampus':
    if pw == '1234':
        print('로그인 성공')
    else:
        print('비밀번호가 일치하지 않습니다.')
else:
    print('아이디 확인')

# 짝수 / 홀수 가려내기
num = int(input('정수 입력 : '))
if num % 2 == 0:
    print('짝수')
else:
    print('홀수')

# 성적
score = int(input('점수 입력 : '))
if score >= 90:
    print('A')
elif score >= 80:
    print('B')
elif score >= 70:
    print('C')
elif score >= 60:
    print('D')
else:
    print('F')