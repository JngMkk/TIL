#!/bin/bash

# 비교할 파일 생성
echo "AAA" > test1.txt
sleep 1s
echo "BBB" > test2.txt

FILE1=test1.txt
FILE2=test2.txt

# 최신 파일인지 비교
if [ $FILE1 -nt $FILE2 ]
then echo True; else echo False; fi

# 예전 파일인지 비교
if [ $FILE1 -ot $FILE2 ]
then echo True; else echo False; fi

# 심볼릭 링크로 연결된 두 개의 파일명을 각각의 변수에 저장
FILE1=/etc/localtime
FILE2=/usr/share/zoneinfo/Asia/Seoul

# 동일한 파일인지 비교
if [ $FILE1 -ef $FILE2 ]
then echo True; else echo False; fi