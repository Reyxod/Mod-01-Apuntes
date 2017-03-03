# !/usr/bin/python
# -*-coding: utf-8-*-

import os

os.system('clear')
salir = False

while salir == False :
	
		os.system('clear')
		edad = raw_input("Introduce tu edad: ")
		
		if not edad.isdigit() :
			
			os.system('clear')
			print "No has introducido un numero\n"
			tecla = raw_input("Pulsa enter para volver a intentar")

		else :
			
			edad = int(edad)
			salir = True
			os.system('clear')
				
			if ( edad >= 18 and edad <= 23 ) or ( edad == 17 ) :
				
				print "Puedes pasar a la sesion de jovenes"
			
			elif edad < 17 :
				
				print "No puedes pasar pequeñin"
				
			elif edad > 23 :
				
				print "Se equivoca, esta no es la sesion de abueletes"
