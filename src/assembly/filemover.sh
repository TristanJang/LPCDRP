#!/bin/bash

file="isolates.txt"
lines=$(cat $file)
for line in $lines
do
	mkdir $line/mummer
	mv $line.* $line/mummer/
done
