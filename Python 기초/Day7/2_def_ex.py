# 연습문제 1
number1 = [3.5, 3.4, 2.0, 4.6]
for n in range(len(number1)):
    number1[n] = round(number1[n])

ls = list(map(round, number1))

# 연습문제 2
ls1 = [1, 2, 3, 4]
ls2 = [10, 20, 30, 40]
def addlist(x, y):
    lst = [x[i] + y[i] for i in range(len(x))]
    print(lst)
    return lst

lst = list(map(lambda x, y: x + y, ls1, ls2))