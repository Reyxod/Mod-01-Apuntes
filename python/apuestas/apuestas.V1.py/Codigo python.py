# !/usr/bin/python
# -*-coding: utf-8-*-

###############
#   Imports   #
###############

import os
from random import randint

#################
#   Variables   #
#################

salir1 = False
salir2 = False 
saldo = 100
palo = {1:"Corazones",2:"Trevoles",3:"Picas",4:"Diamantes"}
carta = {2:"2",3:"3",4:"4",5:"5",6:"6",7:"7",8:"8",9:"9",10:"10",11:"J",12:"Q",13:"K",14:"A"}

###############
#   Nivel 3   #
###############

def mano_jugador():
	
	jcarta = randint(2,14)
	jpalo = randint(1,4)
	jugador = carta[jcarta]+" de "+palo[jpalo]

def mano_maquina():
	
	mcarta = randint(2,14)
	mpalo = randint(1,4)
	maquina = carta[mcarta]+" de "+palo[mpalo]

def ganador():
	
	if jcarta == mcarta :
	
		print "El jugador ha sacado",jugador,"y la maquina",maquina," --> Es un empate"
	
	elif jcarta > mcarta :
		
		print "El jugador ha sacado",jugador,"y la maquina",maquina," --> El jugador gana"
		saldo = saldo + (apuesta * 2)

	else :
		
		print "El jugador ha sacado",jugador,"y la maquina",maquina," --> La maquina gana"
	
##############
#   Nivel 2  #
##############

def apuesta():
	
	while salir1 == False :
	
		print "Tienes este saldo:",saldo
		apuesta = input("\nIntroducir apuesta: ")
		if apuesta == -1 or saldo < 10 :
		
			salir1 == True
			salir2 == True
		
		elif apuesta < 10 or apuesta > saldo :
			
			print "Esa apuesta no esta permitida. Tiene de ser mayor a 10 o menor a tu saldo\n"
		
		else :
			
			salir1 == True
			saldo = saldo - apuesta
		
def jugada():
	
	mano_jugador()
	
	mano_maquina()
	
	ganador()
	
###############
#   Nivel 1   #
###############

while salir2 == False :
	
	apuesta()
	
	jugada()



