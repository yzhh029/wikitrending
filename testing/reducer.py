#!/usr/bin/env python

import sys

current_name = None
current_count = 0
current_date = None
word = None

for line in sys.stdin:
	line = line.strip()
	rd = line.split('\t')
	if len(rd) != 3:
		continue
	name, views, date = rd[0], rd[1], rd[2]

	try:
		count = int(views)
	except ValueError:
		continue
	
	if current_name == name and current_date == date:
		current_count += count
	else:
		if current_name:
			print '%s\t%s\t%s' % (current_name, current_count, current_date)
		current_count = count
		current_name = name
		current_date = date

if current_name == name:
	print '%s\t%s\t%s' % (current_name, current_count, current_date)

