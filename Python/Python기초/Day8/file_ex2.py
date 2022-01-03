# 단어 수 출력
with open('yesterday.txt', 'r') as f:
    a = f.read().lower().replace('\n',' ').replace(',', '')
lst = []
for i in a.split():
    lst.append(i)

my_set = set()
for i in lst:
    my_set.add(i)
my_set = sorted(my_set)
print(my_set)

with open('output.txt', 'w') as f:
    for s in my_set:
        f.write(f"'{s}' : {lst.count(s)}\n")