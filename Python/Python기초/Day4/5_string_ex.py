# 이메일 검사
email = input('이메일 입력 : ')
a = email.find('@')
b = email.find('.')
err = '이메일 형식이 아닙니다.'
if a == -1 or b == -1:
    print(err)
    print('입력한 이메일 :', email)
elif a > b:
    print(err)
    print('입력한 이메일 :', email)
elif email[a:b] == '@':
    print(err)
    print('입력한 이메일 :', email)
elif a == 0:
    print(err)
    print('입력한 이메일 :', email)
elif email[b:] == '.':
    print(err)
    print('입력한 이메일 :', email)
elif email.count('@') > 1:
    print(err)
    print('입력한 이메일 :', email)
elif email.count('.') > 1:
    print(err)
    print('입력한 이메일 :', email)
else:
    print('이메일 형식입니다.')


# 숫자만 추출, 총 합계 구하기
str_data = "{a1:20},{a2:30},{a3:15}, \
 {a4:50},{a5:-14},{a6:15},\
 {a7:20},{a8:70},{a9:-100}"
data = str_data.split(',')
nums = []
for d in data:
    num = d.split(':')[1].split('}')[0]
    nums.append(int(num))
print(sum(nums))


# 입력한 숫자만큼의 하트 출력
tmp = input('숫자를 여러개 입력하세요.')
for i in tmp:
    num = int(i)
    print('\u2665' * num)