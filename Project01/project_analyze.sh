#!/bin/bash

if [ "$#" -eq 0 ] || [ "$#" -gt 8 ] ; then
        echo "error try again"
        exit
fi


if [ "$1" == feature1 ]; then
        ls -lR | grep '^-' | sort -k 5 -rn
fi

if [ "$2" == feature2 ]; then
        parent_path=$( cd "$(dirname "$BASH_SOURCE[0]}")" ; pwd -P ) 
        read -p "Find File Extension: " ext
        find "$parent_path"*."$ext" | wc -l
fi

if [ "$3" == feature3 ]; then 
        :> fixme.log
        find -type f -print0 | while IFS= read -d '' file
        do
                tail -1 $file | grep -q "#FIXME"
                if [ "$?" -eq 0 ] ; then
                        echo "$(filename $file)" >> fixme.log
                fi
        done
fi

if [ "$4" == feature4 ]; then
        if ! [ -f "permissions.log" ] ; then
                :> permissions.log
        fi

        read -p "Change or Restore File: " prompt
        if [ $prompt = "change" ] ; then
                :> permissions.log
                find .. -type f -name "*.sh" -print0 | while IFS= read -d '' file
                do

                        echo "$file"
                        original=$(stat -c "%a %n" "$file")
                        groups=(u g o)
                        for ((n=3 ; n < 10 ; n +=3)); do
                                count=$(echo "scale=0;$n / 3 - 1" | bc - l)
                                if [ $(ls -l "$file" | cut -d ' ' -f 1 | cut -c $n) = "w" ] ; then
                                        chmod "${groups[$count]}+x" "$file"
                                else
                                        chmod "${groups[$count]}-x" "$file"
                                fi
                        done
                        echo "$original" >> permissions.log
                done
        elif [ $prompt = "restore" ] ; then
                while IFS= read -r line
                do
                        IFS=' ' read original file <<< $line
                        chmod "$original" "$file"
                done <<< $(cat "./permissions.log")
        else
                echo "invalid input"
        fi

fi

if [ "$5" == feature5 ] ; then
        :> tag.log
        read -p "type in a tag: " prompt
        find .. -type f -name "*.py" -print0 | while IFS= read -d '' file
        do
                egrep "^#.*${prompt}.*" $file
        done
fi

if [ "$6" == feature6 ] ; then
        gitlog=$(git log -1 --oneline | grep -i 'merge')
fi

if [ "$7" == feature7 ]; then
        sorted=$(ps -eo user,pid,pri,ni,cmd --sort=-priority)
fi

if [ "$8" == feature8 ]; then
       find .. -type f -exec uniq -u {} \; > removedlines.log
fi
