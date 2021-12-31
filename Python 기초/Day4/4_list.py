# 리스트
# 집합적 자료형 : 여러 개의 원소를 가지는 데이터
# 가변적 : 삽입, 삭제, 변경
# 다양한 형식의 데이터 : 숫자, 문자열, 논리형

ls1 = [1, 2, 3]
a, b, c = ls1
print(a, b, c)

ls2 = ['hi', 'bye', 'hello']
ls3 = [ls1, ls2]
print(ls3)
ls4 = ls1 + ls2
print(ls4)
ls1.extend(ls2)
print(ls1)

# 리스트 복사

# 얕은 복사(shallow copy) : 실제 리스트가 복사되지 않고 참조값(주소)만 복사
a = [1, 2, 3, 4]
b = a
print(a)
print(b)

a[-1] = 100
print(a)
print(b)        # 파이썬은 주소를 참조하므로 b도 바뀜. 반대도 마찬가지.

# 깊은 복사(deep copy)
# 리스트 복사본을 새로 생성하여 반환
# list() 함수 또는 copy모듈의 deepcopy() 함수 사용
a = [3, 4, 5, 6]
c = list(a)
print(c)
c[0] = 'apple'      # 리스트 a에 영향을 주지 않음.
print(a)
print(c)

import copy

d = ['a', 'b', 'c']
e = copy.deepcopy(d)
d[0] = 1            # 리스트 e에 영향을 주지 않음.
print(d)
print(e)

# count() : 리스트 내의 특정한 요소 개수 세기
a = [1, 2, 3, 4, 3, 3, 5]
print(a.count(3))

# append(), insert()
a.append(1)
print(a)
a.insert(0, 3)
print(a)

scores = []
for _ in range(10):
    scores.append((int(input('점수를 입력하세요 : '))))
print(scores)

scores = []
for i in range(10):
    idx = i + 1
    scores.append(int(input(f'학생{idx} 점수 입력 : ')))
tot = sum(scores)
avg = sum(scores) / len(scores)
print(f'총점 : {tot}')
print(f'평균 : {avg:.2f}')