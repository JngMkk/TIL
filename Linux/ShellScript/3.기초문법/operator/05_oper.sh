#!/bin/bash

var1=10
var2=10

if (( $var1 > $var2 ))
then
    echo True
else
    echo False
fi

if (( $var1 >= $var2 ))
then
    echo True
else
    echo False
fi

if (( $var1 < $var2 ))
then
    echo True
else
    echo False
fi

if (( $var1 <= $var2 ))
then
    echo True
else
    echo False
fi