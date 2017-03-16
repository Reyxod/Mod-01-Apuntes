# !/usr/bin/python
# -*-coding: utf-8-*-

import os

entrar = True
				
while entrar == True :
	
	try :
		
		entrar = False
		os.system('clear')
		numero1 = float(raw_input("Introduce el primer número: "))
		numero2 = float(raw_input("Introduce el segundo número: "))
		numero3 = float(raw_input("Introduce el tercer número: "))
		os.system('clear')
		
		if ( numero1 == numero2 ) or ( numero1 == numero3 ) or ( numero2 == numero3 ) :
			
			entrar = True
			print "No puedes poner dos números iguales\n"
			tecla = raw_input("Pulsa enter para volver a intentar")	
				
		if ( numero1 > numero2 ) and ( numero1 > numero3 ) :
			
			print "El número mas grande es :",numero1,"\n"
		
		if ( numero2 > numero1 ) and ( numero2 > numero3 ) :
			
			print "El número mas grande es :",numero2,"\n"
			
		if ( numero3 > numero1 ) and ( numero3 > numero2 ) :
			
			os.system('clear')
			print "El número mas grande es :",numero3,"\n"
		
		if ( numero1 < numero2 ) and ( numero1 < numero3 ) :
			
			print "El número mas pequeño es :",numero1
		
		if ( numero2 < numero1 ) and ( numero2 < numero3 ) :
			
			print "El número mas pequeño es :",numero2
			
		if ( numero3 < numero1 ) and ( numero3 < numero2 ) :
			
			print "El número mas pequeño es :",numero3
			
	except ValueError :
		
		entrar = True
		os.system('clear')
		print "Eso no es un número\n"
		tecla = raw_input("Pulsa enter para volver a intentar")	
