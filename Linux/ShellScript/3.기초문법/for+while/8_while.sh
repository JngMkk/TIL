#!/bin/bash

# 변수 num이 3보다 작은 경우에 num 값을 출력하는 예

num=0

while [ $num -lt 3 ]
do
    echo $num
    num=$((num+1))
done