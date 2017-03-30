# !/usr/bin/python
# -*-coding: utf-8-*-

import os

numero = 1
salir = False

os.system('clear')
turno = input("Introduce cuantos turnos quieres hacer: ")
os.system('clear')

direccion = raw_input("Introduce la direccion de este turno: ")  

while salir == False :
	
	if numero % 8 == 1 or numero % 8 == 2 :  
		
		print numero,"Mover arriba"
		
	if numero % 8 == 3 or numero % 8 == 4 :
		
		if direccion == "D" : 
		
			print numero,"Mover derecha"
		
		else :
			
			print numero,"Mover izquierda"
		
	if numero % 8 == 5 or numero % 8 == 6 :
		
		print numero,"Mover abajo"
		
	if numero % 8 == 7 or numero % 8 == 0 :
	
		if direccion == "D" :
				
				print numero,"Mover izquierda"
			
		else :
			
			print numero,"Mover derecha"
		
	if numero % 8 == 0 : 
		
		turno = turno - 1
		numero = 0
		
		if turno != 0 :
		
			direccion = raw_input("Introduce la direccion de este turno: ")  
		
	if turno == 0 :
		
		salir = True
	
	numero = numero + 1 
