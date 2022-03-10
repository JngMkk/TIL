#!/bin/bash

var1="abc"
var2="def"

if [ $var1 = $var2 ]
then echo True
else echo False
fi

if [ $var1 == $var2 ]
then echo True
else echo False
fi

if [ $var1 != $var2 ]
then echo True
else echo False
fi

if [[ $var1 > $var2 ]]
then echo True
else echo False
fi

if [[ $var1 < $var2 ]]
then echo True
else echo False
fi