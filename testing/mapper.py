#!/usr/bin/env python

import sys, os, re, urllib

record_rx = re.compile('en (.*) ([0-9].*) ([0-9].*)')

namespace_rx = re.compile('(Media|Special' + 
		'|Talk|User|User_talk|Project|Project_talk|File' +
		'|File_talk|MediaWiki|MediaWiki_talk|Template' +
		'|Template_talk|Help|Help_talk|Category' +
		'|Category_talk|Portal|Wikipedia|Wikipedia_talk' +
		'|zh|Book|Book_talk|Ca|Commons|Http|Image)\:(.*)')

file_rx = re.compile('(.*).(jpg|gif|png|JPG|GIF|PNG|txt|ico)')

blacklist = [
		'404_error',
		'Main_Page']
blackns = [
		'Media', 'Special', 'Talk', 'User', 'User_talk', 'Project', 'Project_talk', 'File',
		'File_talk', 'MediaWiki', 'MediaWiki_talk', 'Template', 'Template_talk', 'Help', 'Help_talk',
		'Category', 'Category_talk', 'Portal', 'Wikipedia', 'Wikipedia_talk', 'zh', 'ja', 'Book', 'Book_talk',
		'Ca']

def checkTitle(title):
	ns_match = namespace_rx.match(title)
	if ns_match is not None:
		return False
	file_match = file_rx.match(title)
	if file_match is not None:
		return False

	for black in blacklist:
		if title.find(black) >= 0:
			return False
	#for ns in blackns:
	#	ns = ns + ':'
	#	if title.find(ns) == 0:
	#		return False
	return True

try:
	filepath = os.environ['mapreduce_map_input_file']
	filename = os.path.split(filepath)[-1]
except KeyError:
	filename = 'pagecounts-20110101-000000.gz'

date = filename.split('-')[1]
#date = date[:4] + '-' + date[4:6] + '-' + date[-2:]

for line in sys.stdin:
	rd_match = record_rx.match(line)
	if rd_match is not None:
		rd = line.split(' ')
		title, count = rd[1], rd[2]
		if checkTitle(title):
			title = urllib.unquote_plus(title)
			title_en = str(title)
			if checkTitle(title_en):
				print '%s\t%s\t%s' % (title_en, count, date)


