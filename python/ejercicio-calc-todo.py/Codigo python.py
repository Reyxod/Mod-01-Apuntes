# !/usr/bin/python
# -*-coding: utf-8-*-

import os

salir = False

#Definiciones de las operaciones

def suma() :
	
	entrar = True
				
	while entrar == True :
		
		try :
			
			numero1 = float(raw_input("Introduce un número: "))
			numero2 = float(raw_input("Introduce un número: "))
			entrar = False
			os.system('clear')
			
		except ValueError :
			
			os.system('clear')
			print "Eso no es un número\n"
			tecla = raw_input("Pulsa enter para volver a intentar")	
			os.system('clear')

	sumar = numero1 + numero2
	print "El resultado de",numero1,"+",numero2,"=",sumar
	tecla = raw_input("\nPulsa enter para volver al menu")
		
def resta() :
	
	entrar = True
				
	while entrar == True :
		
		try :
			
			numero1 = float(raw_input("Introduce un número: "))
			numero2 = float(raw_input("Introduce un número: "))
			entrar = False
			os.system('clear')
			
		except ValueError :
			
			os.system('clear')
			print "Eso no es un número\n"
			tecla = raw_input("Pulsa enter para volver a intentar")	
			os.system('clear')

	restar = numero1 - numero2
	print "El resultado de",numero1,"-",numero2,"=",restar
	tecla = raw_input("\nPulsa enter para volver al menu")
	
def multiplicacion() :
	
	entrar = True
				
	while entrar == True :
		
		try :
			
			numero1 = float(raw_input("Introduce un número: "))
			numero2 = float(raw_input("Introduce un número: "))
			entrar = False
			os.system('clear')
			
		except ValueError :
			
			os.system('clear')
			print "Eso no es un número\n"
			tecla = raw_input("Pulsa enter para volver a intentar")	
			os.system('clear')

	multiplicar = numero1 * numero2
	print "El resultado de",numero1,"*",numero2,"=",multiplicar
	tecla = raw_input("\nPulsa enter para volver al menu")

def division() :
	
	entrar = True
				
	while entrar == True :
		
		try :
			
			numero1 = float(raw_input("Introduce un número: "))
			numero2 = float(raw_input("Introduce un número: "))
			os.system('clear')
			
			if numero2 == 0 :
				
				print "No se puede dividir por zero\n"
				tecla = raw_input("Pulsa enter para volver a intentar")
				os.system('clear')
				
			else :
				
				entrar = False
			
		except ValueError :
			
			os.system('clear')
			print "Eso no es un número\n"
			tecla = raw_input("Pulsa enter para volver a intentar")	
			os.system('clear')
		
	dividir = numero1 / numero2
	print "El resultado de",numero1,"/",numero2,"=",dividir
	tecla = raw_input("\nPulsa enter para volver al menu")	

#Codigo de menu de la calculadora

while salir == False :
		
		os.system('clear')
		print "Calculadora \n \n1-Sumar \n2-Restar \n3-Multiplicar \n4-Dividir \n5-Salir \n" 
		opcion = raw_input("Introduce una opcion: ")
		os.system('clear')
		
		if not opcion.isdigit() :
			
			print "No has introducido un numero\n"
			tecla = raw_input("Pulsa enter para volver a intentar")
		
		else :
			
			opcion = int(opcion)
				
			if opcion == 1 :
			
				suma()
			
			elif opcion == 2 :
				
				resta()
				
			elif opcion == 3 :
				
				multiplicacion()
				
			elif opcion == 4 :
				
				division()
			
			elif opcion == 5 :
				
				salir = True
				os.system('clear')
				
			elif ( opcion < 1 or opcion > 5 ) :
				
				print "Esta opcion no esta contemplada\n"
				tecla = raw_input("Pulsa enter para volver a intentar")

