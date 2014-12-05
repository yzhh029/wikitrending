#!/bin/bash

HADOOP=hadoop
STREAMING=/home/hadoop/contrib/streaming/hadoop-streaming.jar
MAPPER=./mapper.py
REDUCER=./reducer.py

INPUT=/onedaytest
OUTPUT=/onedayout

$HADOOP jar $STREAMING -file $MAPPER -file $REDUCER -mapper $MAPPER -reducer $REDUCER -input $INPUT -output $OUTPUT
