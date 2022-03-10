#!/bin/bash

# /etc/localtime의 파일 속성 확인
ls -l /etc/localtime

# /etc/localtime 원파일의 속성 확인
ls -l /usr/share/zoneinfo/Asia/Seoul

FILE=/etc/localtime

# 스크립트 실행 소유자와 같은지
if [ -O $FILE ]
then echo True; else echo False; fi

# 소유 그룹이 같은지
if [ -G $FILE ]
then echo True; else echo False; fi