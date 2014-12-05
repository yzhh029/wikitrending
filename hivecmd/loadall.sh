#!/bin/bash

date=20110101

while test $date -ne 20110132
do
	echo 'load ' $date ' data'
	hive  -hiveconf CURRENT_DATE=$date -f loopload.sql -v
	date=$[ $date + 1]
done
