# 숫자 더하기

"""
한 줄에 두 개의 숫자가 저장되어 있는 파일을 읽어와서
한 줄의 두 숫자를 더한 연산 결과를 파일로 저장하기
"""

def sum(inputname, savename):
    except_str = ''
    with open(inputname, 'r') as f:
        a = f.readlines()
    ls = [i.split('\n')[0] for i in a]
    ls = [i for i in ls if i != except_str]
    ls = [i.split(' ') for i in ls]
    with open(savename, 'w') as f:
        for l in ls:
            f.write(f'{l[0]}+{l[1]}={float(l[0]) + float(l[1])}\n')

if __name__ == '__main__':
    sum('num.txt', 'calc.txt')
