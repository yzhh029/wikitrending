#!/usr/bin/env python

import sys, re

blackns = [
	'Media', 'Special', 'Talk', 'User', 'User_talk', 'Project', 'Project_talk', 'File',
	'File_talk', 'MediaWiki', 'MediaWiki_talk', 'Template', 'Template_talk', 'Help', 'Help_talk',
	'Category', 'Category_talk', 'Portal', 'Wikipedia', 'Wikipedia_talk', 'zh', 'ja', 'Book', 'Book_talk',
	'Ca']

namespace_rx = re.compile('(Media|Special' + 
	'|Talk|User|User_talk|Project|Project_talk|File' +
	'|File_talk|MediaWiki|MediaWiki_talk|Template' +
	'|Template_talk|Help|Help_talk|Category' +
	'|Category_talk|Portal|Wikipedia|Wikipedia_talk' +
	'|zh|Book|Book_talk|Ca)\:(.*)')

for line in sys.stdin:
	rd = line.split('\t')
	name = rd[0]
	match = namespace_rx.match(name)
	if match is not None:
		print line + " match"
	
	for ns in blackns:
		if line.find(ns+':') == 0:
			print line + " find"
