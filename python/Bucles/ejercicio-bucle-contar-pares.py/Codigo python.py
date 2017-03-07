# !/usr/bin/python
# -*-coding: utf-8-*-

import os
os.system('clear')

numero = 1
numero2 = 1
salir = False

while salir == False :
			
	try :
		
		limite = int(raw_input("Contar desde el 1 hasta el: "))
	
		if limite == 0 :
			
			os.system('clear')
			print "No se puede poner 0\n"
			tecla = raw_input("Pulsa enter para volver a intentar")	
			os.system('clear')
		
		elif limite < 0 :
			
			os.system('clear')
			print "No se puede poner un número negativo\n"
			tecla = raw_input("Pulsa enter para volver a intentar")	
			os.system('clear')
			
		else :
			
			salir = True
			os.system('clear')
			
			### Aqui es la parte del bucle del ejercicio
			
			while numero <= limite :
				
				if numero == 2 :
					
					numero2 = 2
				
				print numero
				numero = numero + numero2
			
			###
				
	except ValueError :
		
		os.system('clear')
		print "Eso no es un número\n"
		tecla = raw_input("Pulsa enter para volver a intentar")	
		os.system('clear')
