# 숫자 더하기

"""
한 줄에 두 개의 숫자가 저장되어 있는 파일을 읽어와서
한 줄의 두 숫자를 더한 연산 결과를 파일로 저장하기
"""

def sum(inputname, savename):
    with open(inputname, 'r') as f:
        tmp = f.read().replace('\n', ' ')
    lst = tmp.split()
    a, b = lst[0::2], lst[1::2]
    lst2 = [[a[i], b[i]] for i in range(len(a))]
    
    with open(savename, 'w') as f:
        for ls in lst2:
            val1 = int(ls[0])
            val2 = int(ls[1])
            f.write(f'{val1}+{val2}={float(val1 + val2)}\n')

if __name__ == '__main__':
    sum('num.txt', 'calc.txt')
