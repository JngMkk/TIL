#!/bin/bash

# 배열을 사용할 때는 ${배열[@]}로 표현해야 배열의 모든 아이템을 사용할 수 있음

array=("apple" "banana" "pineapple")

for fruit in ${array[@]}
do
    echo $fruit;
done