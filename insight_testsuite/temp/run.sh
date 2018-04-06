#!/bin/bash
#
# Use this shell script to compile (if necessary) your code and then execute it. Below is an example of what might be found in this file if your program was written in Python
# 

python ./src/sessionization.py ./input/log.csv ./input/inactivity_period.txt ./output/sessionization.txt

# one loop through
#time wc -l ./input/log20170630.csv
# check process times  
#for i in `seq 1 3`;
#do 
#var=$((10**i)) 
# creates output file for decimated file
#echo "decimate text by: " $var
#suffix="$( printf -- '-%02d' "$var" )"
#outputfile="./output/sessionization$suffix.txt"
#echo "output file path: " $outputfile
# decimated file
# decimate='0~'$var'p'
#outputcsv="./input/log$suffix.csv"
#echo "the input decimated csv file: " $outputcsv
#time awk '(!(NR%'$var')||(NR==1))'  ./input/log20170630.csv > $outputcsv
#time python ./src/sesh2.py $outputcsv ./input/inactivity_period.txt $outputfile 
#done
