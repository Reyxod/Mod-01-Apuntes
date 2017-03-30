# !/usr/bin/python
# -*-coding: utf-8-*-

import os

os.system('clear')

numero = 1
salir = False
turno = 1

while salir == False :
	
	if numero % 8 == 1 or numero % 8 == 2 :  
		print numero,"Mover arriba"
		
	if numero % 8 == 3 or numero % 8 == 4 :
		
		print numero,"Mover derecha"
		
	if numero % 8 == 5 or numero % 8 == 6 :
		
		print numero,"Mover abajo"
		
	if numero % 8 == 7 or numero % 8 == 0 :
		
		print numero,"Mover izquierda"
		
	if numero % 8 == 0 : 
		
		turno = turno + 1
		numero = 0
		
	if turno == 3 :
		
		salir = True
	
	numero = numero + 1
