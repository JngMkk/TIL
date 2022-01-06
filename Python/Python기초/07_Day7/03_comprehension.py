# list comprehension
a = [i for i in range(10)]
print(a)

# 짝수만
a = [i for i in range(10) if i % 2 == 0]
print(a)

b = [i if i % 2 == 0 else -10 for i in range(10)]
print(b)

# 중첩 반복문
ls1 = ['a', 'b', 'c']
ls2 = ['D', 'E', 'F']

a = []
for i in ls1:
    for j in ls2:
        a.append(i + j)
print(a)

a = [i + j for i in ls1 for j in ls2]
print(a)
a = [i + j for i in ls1 for j in ls2 if not i == j]
print(a)

words = 'Remember to let her into your heart'.split()
print(words)
word_len = [(w.upper(), w.lower(), len(w)) for w in words]
print(word_len)