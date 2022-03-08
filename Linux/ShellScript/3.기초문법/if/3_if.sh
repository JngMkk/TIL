#!/bin/bash

# 변수 value의 길이가 0인지 비교하는 조건문
# 연산자 -z는 변수에 저장된 값의 길이가 0인지 비교하여 0이면 True, 아니면 False 리턴하는 문자열 연산자

value=""
if [ -z $value ]
then
    echo True
else
    echo False
fi