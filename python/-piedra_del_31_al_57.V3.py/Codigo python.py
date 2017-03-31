# !/usr/bin/python
# -*-coding: utf-8-*-

import os

os.system('clear')

numero = 31
partidas = 1
empate = 0
gana1 = 0
gana2 = 0
piedra = 0
papel = 0
tijeras = 0
salir = False

while salir == False :
	
	if numero % 7 == 0 or numero % 7 == 1 :  
		
		jugador1 = "Tijeras"
		tijeras = tijeras + 1
		
	elif numero % 7 == 2 or numero % 7 == 3 or numero % 7 == 6 :
		
		jugador1 = "Piedra "
		piedra = piedra + 1
		
	elif numero % 7 == 4 or numero % 7 == 5 :
		
		jugador1 = "Papel  " 
		papel = papel + 1 
	
	if numero % 5 == 0 or numero % 5 == 1 or numero % 5 == 2 :
		
		jugador2 = "Papel  "
		papel = papel + 1  
	
	elif numero % 5 == 3 :
		
		jugador2 = "Tijeras"
		tijeras = tijeras + 1
	
	elif numero % 5 == 4 :
		
		jugador2 = "Piedra "
		piedra = piedra + 1 
		
	if jugador1 == jugador2 :
	
		print numero,"El primer jugador saca",jugador1,"y el segundo",jugador2,"--> Es un empate"
		empate = empate + 1
	
	elif ( jugador1 == "Piedra " and jugador2 == "Tijeras" ) or ( jugador1 == "Tijeras" and jugador2 == "Papel  " ) or ( jugador1 == "Papel  " and jugador2 == "Piedra " ) :
		
		print numero,"El primer jugador saca",jugador1,"y el segundo",jugador2,"--> El primer jugador gana"
		gana1 = gana1 + 1
	
	else :
		
		print numero,"El primer jugador saca",jugador1,"y el segundo",jugador2,"--> El segundo jugador gana" 
		gana2 = gana2 + 1
		
	if numero == 57 :
		
		porcetaje_j1 = str((gana1 * 100) / partidas) + "%"
		porcetaje_j2 = str((gana2 * 100) / partidas) + "%"
		porcetaje_empate = str((empate * 100) / partidas) + "%"
		
		salir = True
		print "\nHan hecho",partidas,"partidas"
		print "Han empatado",empate,"veces, que es un",porcetaje_empate,"de las veces"
		print "El primer jugador ha ganado",gana1,"veces, que es un",porcetaje_j1,"de las veces"
		print "El segundo jugador ha ganado",gana2,"veces, que es un",porcetaje_j2,"de las veces"
		print "La piedra se ha usado",piedra,"veces"
		print "El papel se ha usado",papel,"veces"
		print "Las tijeras se han usado",tijeras,"veces"
	
	numero = numero + 1
	partidas = partidas + 1
