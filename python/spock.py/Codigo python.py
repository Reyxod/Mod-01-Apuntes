# !/usr/bin/python
# -*-coding: utf-8-*-

import os
import random

os.system('clear')

numero = 1
salir = False
lista = ["Piedra","Papel","Tijeras","Lagarto","Spock"]
manorandom1 = lista[random.randrange(5)]
manorandom2 = lista[random.randrange(5)]

while salir == False :

	if manorandom1 == manorandom2 :
	
		print numero,"El primer jugador saca",manorandom1,"y el segundo",manorandom2,"--> Es un empate"
		
	elif (manorandom1 == "Piedra" and (manorandom2 == "Tijeras" or manorandom2 == "Lagarto")) or (manorandom1 == "Papel" and (manorandom2 == "Piedra" or manorandom2 == "Spock")) or (manorandom1 == "Tijeras" and (manorandom2 == "Papel" or manorandom2 == "Lagarto")) or (manorandom1 == "Lagarto" and (manorandom2 == "Spock" or manorandom2 == "Papel")) or (manorandom1 == "Spock" and (manorandom2 == "Tijeras" or manorandom2 == "Piedra")) :
	
		print numero,"El primer jugador saca",manorandom1,"y el segundo",manorandom2,"--> El primer jugador gana"
		salir = True
		
	else :
		
		print numero,"El primer jugador saca",manorandom1,"y el segundo",manorandom2,"--> El segundo jugador gana" 
		salir = True
				
	numero = numero + 1
	manorandom1 = lista[random.randrange(5)]
	manorandom2 = lista[random.randrange(5)]
