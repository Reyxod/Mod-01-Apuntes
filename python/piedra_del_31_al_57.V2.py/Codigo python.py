# !/usr/bin/python
# -*-coding: utf-8-*-

import os

os.system('clear')

numero = 31
salir = False

while salir == False :
	
	if numero % 7 == 0 or numero % 7 == 1 :  
		
		jugador1 = "Tijeras"
		
	elif numero % 7 == 2 or numero % 7 == 3 or numero % 7 == 6 :
		
		jugador1 = "Piedra " #Le pongo el espacio aqui y en la comparacion para que se vea mejor en el print
		
	elif numero % 7 == 4 or numero % 7 == 5 :
		
		jugador1 = "Papel  " #Le pongo el espacio aqui y en la comparacion para que se vea mejor en el print
	
	if numero % 5 == 0 or numero % 5 == 1 or numero % 5 == 2 :
		
		jugador2 = "Papel  " #Le pongo el espacio aqui y en la comparacion para que se vea mejor en el print
	
	elif numero % 5 == 3 :
		
		jugador2 = "Tijeras"
	
	elif numero % 5 == 4 :
		
		jugador2 = "Piedra " #Le pongo el espacio aqui y en la comparacion para que se vea mejor en el print
		
	if jugador1 == jugador2 :
	
		print numero,"El primer jugador saca",jugador1,"y el segundo",jugador2,"--> Es un empate"
	
	elif ( jugador1 == "Piedra " and jugador2 == "Tijeras" ) or ( jugador1 == "Tijeras" and jugador2 == "Papel  " ) or ( jugador1 == "Papel  " and jugador2 == "Piedra " ) :
		
		print numero,"El primer jugador saca",jugador1,"y el segundo",jugador2,"--> El primer jugador gana"
	
	else :
		
		print numero,"El primer jugador saca",jugador1,"y el segundo",jugador2,"--> El segundo jugador gana" 
		
	if numero == 57 :
		
		salir = True
	
	numero = numero + 1
