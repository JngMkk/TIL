# 숫자 더하기

"""
한 줄에 두 개의 숫자가 저장되어 있는 파일을 읽어와서
한 줄의 두 숫자를 더한 연산 결과를 파일로 저장하기
"""

def sum(inputname, savename):
    lst = []
    with open(inputname, 'r') as f:
        a = f.readlines()
        for i in a:
            tmp = i.split('\n')[0]
            if tmp != '':
                lst.append(tmp)
    lst = [i.split() for i in lst]
    
    with open(savename, 'w') as f:
        for ls in lst:
            f.write(f'{ls[0]}+{ls[1]}={float(ls[0]) + float(ls[1])}\n')

if __name__ == '__main__':
    sum('num.txt', 'calc.txt')
