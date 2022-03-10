#!/bin/bash

var1=10
var2=10

if [ $var1 -gt $var2 ]
then
    echo True
else
    echo False
fi

if [ $var1 -ge $var2 ]
then
    echo True
else
    echo False
fi

if [ $var1 -lt $var2 ]
then
    echo True
else
    echo False
fi

if [ $var1 -le $var2 ]
then
    echo True
else
    echo False
fi