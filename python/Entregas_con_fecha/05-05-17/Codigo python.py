#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

os.system('clear') 

for fila in xrange(1,6):
	print ""
	for columna in xrange(1,5):
		if fila == 1:			
			if columna == 2:
				print "A",
			elif columna == 3:
				print "B",
			elif columna == 4:
				print "C",
			else:
				print "-",
	
		elif columna == 1:
			print fila-1,
		else:
			print "-",
