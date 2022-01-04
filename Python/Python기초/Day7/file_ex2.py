# 단어 수 출력
with open('yesterday.txt', 'r') as f:
    a = f.read().lower().replace(',', '')
lst = a.split()

my_set = set(lst)
my_set = sorted(my_set)

with open('output.txt', 'w') as f:
    for s in my_set:
        f.write(f"'{s}' : {lst.count(s)}\n")

# 강사님 해답
f = open('yesterday.txt', 'r')
yesterday = f.readlines()
f.close()

words = []
for line in yesterday:
    for w in line.split():
        words.append(w.lower())

wordL = list(set(words))
wordL.sort()

wordDict = dict()
for w in wordL:
    wordDict[w] = words.count(w)

for w in wordDict.ites():
    print(w)