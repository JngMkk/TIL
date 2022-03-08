#!/bin/bash

# 변수 value의 값은 0보다 크고, 10보다 작은지를 비교하는 조건문
# 연산자 -gt는 A가 B보다 큰지를 비교하는 연산자이며,
# 연산자 -lt는 A가 B보다 작은지를 비교하는 연산자.
# &&는 AND 연산을 의미함.

value=5
if [ $value -gt 0 ] && [ $value -lt 10 ]
then
    echo True
else
    echo False
fi