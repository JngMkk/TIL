# 단어 수 출력
except_str = ''
my_set = set()
ls = []
with open('yesterday.txt', 'r') as f:
    while True:
        a = f.readline()
        ls.append(a.lower().split('\n')[0].split(' '))
        if not a:
            break
ls = [i for i in ls if i[0] != except_str]
my_list = sum(ls, [])

for l in my_list:
    my_set.add(l)

with open('output.txt', 'w') as f:
    for s in my_set:
        f.write(f"'{s}' : {my_list.count(s)}\n")