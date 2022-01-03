# 로그파일 작성
import os, datetime, random

if not os.path.isdir('log'):
    os.mkdir('log')

if not os.path.exists('log/countLog.txt'):
    f = open('log/countLog.txt', 'w')
    f.write('Record Start\n')
    f.close()

with open('log/countLog.txt', 'a') as f:
    for _ in range(10):
        stamp = str(datetime.datetime.now())
        value = random.random() * 1000000
        log_line = stamp + '\t' + str(value) + '\tmake value\n'
        f.write(log_line)