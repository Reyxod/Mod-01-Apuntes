# !/usr/bin/python
# -*-coding: utf-8-*-

import os

salir = False

while salir == False :
			
	try :
		
		os.system('clear')
		limite = int(raw_input("Empezando desde -1 sumar 1 estas veces: "))
		os.system('clear')
		
		if limite == 0 :
			
			print "No se puede poner 0\n"
			tecla = raw_input("Pulsa enter para volver a intentar")	
		
		elif limite < 0 :
			
			print "No se puede poner un número negativo\n"
			tecla = raw_input("Pulsa enter para volver a intentar")	
			
		else :
			
			salir = True
			
			### Aqui es la parte del bucle del ejercicio
			
			print 0
			
			for x in range( limite -1 ) :
 
				print x + 1
				
			### 
	
	except ValueError :
		
		os.system('clear')
		print "Eso no es un número\n"
		tecla = raw_input("Pulsa enter para volver a intentar")	
