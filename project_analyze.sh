#!/bin/bash

if [ "$#" -eq 0 ] || [ "$#" -gt 3 ] ; then
	echo "error try again"
	exit
fi


if [ "$1" == feature1 ]; then
	ls -lR | grep '^-' | sort -k 5 -rn
fi

if [ "$2" == feature2 ]; then 
	read -p "Find File Extension: " ext
	find ~/private/CS1XA3/*."$ext" | wc -l
fi

if [ "$3" == feature3 ]; then 
	:> fixme.log
	find -type f -print0 | while IFS= read -d '' file
	do
		tail -1 $file | grep -q "#FIXME"
		if [ "$?" -eq 0 ] ; then
			echo "$(filename $file)" >> fixme.log
		fi

