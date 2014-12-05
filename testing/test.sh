#!/bin/bash

cat pagecounts-20110101-000000 | ./mapper.py | head -n 100 | sort | ./reducer.py
