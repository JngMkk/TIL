# Set : 집합 형태의 자료 구조
# 중복 허용 x
# 원소들 사이에 순서가 없음. 선형 자료구조가 아님
s1 = {1, 2, 3, 4, 5}
s2 = set([3, 4, 7, 8, 9])
print(type(s1))
print(dir(s2))

# 하나씩 추가
s2.add(10)
print(s2)

# 여러 개 추가
s2.update([6,7])
print(s2)

# 집합 안에 리스트 포함 x, 튜플 포함 o
s3 = {1, 2, (3, 4)}
print(s3)

# 요소 삭제
s3.remove(1)    # 없으면 Error
print(s3)
s3.discard(1)   # 없어도 Error x
print(s3)

# 교집합
s4 = s1.intersection(s2)
print(s4)
s4 = s1 & s2
print(s4)

# 합집함
s4 = s1 | s2
print(s4)
s4 = s1.union(s2)
print(s4)

# 차집합
s4 = s1 - s2
print(s4)
s4 = s2 - s1
print(s4)
s4 = s1.difference(s2)
print(s4)
