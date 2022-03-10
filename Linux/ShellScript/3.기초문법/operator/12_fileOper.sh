#!/bin/bash

FILE=/etc/localtime

if [ -f $FILE ]
then echo True
else echo False
fi

if [ -L $FILE ]
then echo True
else echo False
fi