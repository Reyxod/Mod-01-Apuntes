# !/usr/bin/python
# -*-coding: utf-8-*-

# He utilizado este metodo para comprovar si insertaban un numero o no
# porque de la otra forma daba error al poner un numero negativo. 

import os

os.system('clear')
salir = False
				
while salir == False :
	
	try :
		
		numero = int(raw_input("Introduce un número: "))
		os.system('clear')
		salir = True
			
		if numero % 2 == 0 :
				
			print "Qué bonito número par"
			
		elif numero % 2 != 0 :
				
			print "Qué número más vulgar"
	
	except ValueError :
		
		os.system('clear')
		print "Eso no es un número\n"
		tecla = raw_input("Pulsa enter para volver a intentar")	
		os.system('clear')
