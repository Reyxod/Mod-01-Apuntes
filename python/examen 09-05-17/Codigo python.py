#!/usr/bin/env python
# -*- coding: utf-8 -*-

def mi_rango(inicio,final,incremento):
	
	if inicio <= final :
		
		while inicio <= final :
			
			yield inicio
			
			inicio = inicio + incremento
			
	else:
		
		while inicio >= final :
			
			yield inicio
			
			inicio = inicio - incremento
			
for fila in mi_rango(1,4,1):
	
	for columna in mi_rango(1,8,1):
		
		if ( fila == 1 ) or ( fila == 4 ) or ( columna == 1 ) or ( columna == 8 ) :
			
			print "*",
		
		else :
			
			if ( fila == 2 and ( columna == 4 or columna == 5 ) ) :
				
				print "·",
				
			elif ( fila == 3 and columna == 4 ) :
				
				print "\\",	
			
			elif ( fila == 3 and columna == 5 ) :
				
				print "/",
			
			else : 
				
				print " ",
				
	print ""
