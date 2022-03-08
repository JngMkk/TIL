#!/bin/bash

# 입력받은 파라미터에 따라 해당 문자열을 출력하는 예제

case $1 in
    start)
    echo "start";;
    stop)
    echo "stop";;
    restart)
    echo "restart";;
    help)
    echo "help";;
    *)
    echo "Please input sub command"
esac
