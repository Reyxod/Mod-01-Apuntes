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
			
for fila in mi_rango(1,8,1):
	
	for columna in mi_rango(1,8,1):
		
		if ( fila + columna ) % 2 == 0 :
			
			print "*",
		
		else :
			
			print " ",
					
	print ""
