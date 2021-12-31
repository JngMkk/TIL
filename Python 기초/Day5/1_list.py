scores = [90, 78, 81, 65, 99]
print(scores)
scores.sort()                       # 오름차순 정렬
print(scores)


scores = [90, 78, 81, 65, 99]
scores.sort(reverse = True)         # 내림차순 정렬
print(scores)

scores = [90, 78, 81, 65, 99]
scores.reverse()                    # 리스트 역순
print(scores)

scores = [90, 78, 81, 65, 99]
print(sorted(scores))               # 오름차순 정렬, inplace = False
print(sorted(scores, reverse = True))

chr = ['b', 'A', 'e', 'C']          # ASCII 코드값 : A(65) / a(97)
chr.sort(key = str.lower)           # 대소문자 구별 없이
print(chr)

data = [[1,2,3,4,5], [6,7,8,9,10], [11,12,13,14,15]]
row = len(data); col = len(data[0])

for r in range(row):
    for c in range(col):
        print(data[r][c], end = '\t')
    print()
