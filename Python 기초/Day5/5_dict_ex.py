students = [{'name' : '홍길동', 'korean' : 87, 'math' : 98, 'english' : 88, 'science' : 95},
            {'name' : '이몽룡', 'korean' : 92, 'math' : 98, 'english' : 96, 'science' : 98},
            {'name' : '성춘향', 'korean' : 76, 'math' : 96, 'english' : 94, 'science' : 90},
            {'name' : '변학도', 'korean' : 98, 'math' : 92, 'english' : 96, 'science' : 92},
            {'name' : '박지성', 'korean' : 95, 'math' : 98, 'english' : 98, 'science' : 98},
            {'name' : '류현진', 'korean' : 64, 'math' : 88, 'english' : 92, 'science' : 92}]

print('이름\t총점\t평균')
for s in students:
    name = s.get('name')
    ls = list(s.values())
    tot = sum(ls[1:])
    avg = tot / len(ls[1:])
    print(name,'\t',tot,'\t',avg)



d = {}
while True:
    key = input('영어 단어 등록 (종료는 quit) : ')
    key = key.lower()
    if key == 'quit':
        break
    elif key not in d:
        val = input(f'{key}의 뜻입력 (종료는 quit) : ')
        d[key] = val
    else:
        print(f'{key}는 이미 등록된 단어 입니다.')

while True:
    word = input('검색할 단어 입력 (종료는 quit) : ')
    if word == 'quit':
        print('종료합니다.')
        break
    elif word not in d:
        print(f'{word}는 사전에 없는 단어 입니다.')
    else:
        print(f'{word}의 뜻은 {d[word]}입니다.')
    