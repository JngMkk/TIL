# gbbGame.py
# 가위바위보 게임
from random import randint

def gbb_game(you_n):
    com = randint(1, 3)
    if com > you_n or com - you_n == -2:
        print('컴퓨터가 이겼습니다.')
    elif com == you_n:
        print('비겼습니다.')
    else:
        print('당신이 이겼습니다.')
    print('Com :', com)

def input_num():
    num = int(input('YOU 입력 (1:가위, 2:바위, 3:보) : '))
    return gbb_game(num)
