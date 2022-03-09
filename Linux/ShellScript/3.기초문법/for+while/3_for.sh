#!/bin/bash

# 환경변수를 사용하여 데릭터리 경로를 for문에 사용

for file in $GOROOT/*
do
    echo $file;
done