#!/bin/bash

if [ -d $HOME ]
then echo True
else echo False
fi

if [ -e $HOME ]
then echo True
else echo False
fi