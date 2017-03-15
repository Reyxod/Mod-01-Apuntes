# !/usr/bin/python
# -*-coding: utf-8-*-

import os

entrar = True
				
while entrar == True :
	
	try :
		
		os.system('clear')
		numero1 = float(raw_input("Introduce el primer número: "))
		numero2 = float(raw_input("Introduce el segundo número: "))
		
	
		if numero1 == numero2 :
			
			os.system('clear')
			print "No puedes poner dos números iguales\n"
			tecla = raw_input("Pulsa enter para volver a intentar")	
			
		if numero1 > numero2 :
			
			os.system('clear')
			print "El número mas grande es :",numero1
			entrar = False
		
		if numero2 > numero1 :
			
			os.system('clear')
			print "El número mas grande es :",numero2
			entrar = False
			
		
	except ValueError :
		
		os.system('clear')
		print "Eso no es un número\n"
		tecla = raw_input("Pulsa enter para volver a intentar")	
		os.system('clear')
