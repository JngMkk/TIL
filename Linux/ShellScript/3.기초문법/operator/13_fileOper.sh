#!/bin/bash

ls -l /etc/localtime

# 원파일 속성 확인
ls -l /usr/share/zoneinfo/Asia/Seoul

FILE=/etc/localtime

# 파일에 읽기 권한이 있으면 True, 아니면 False
if [ -r $FILE ]
then echo True; else echo False; fi

# 파일에 쓰기 권한이 있으면 True, 아니면 False
if [ -w $FILE ]
then echo True; else echo False; fi

# 파일에 실행 권한이 있으면 True, 아니면 False
if [ -x $FILE ]
then echo True; else echo False; fi

# 파일의 크기가 0보다 크면 True, 아니면 False
if [ -s $FILE ]
then echo True; else echo False; fi