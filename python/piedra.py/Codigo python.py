# !/usr/bin/python
# -*-coding: utf-8-*-

import os


os.system('clear')
print "Posibles jugadas:\n\n-Piedra\n-Tijeras\n-Papel\n" 
tecla = raw_input("Dale a enter para empezar")
os.system('clear')
jugador1 = raw_input("JUGADOR-1.Introduce que jugada quieres: ")
os.system('clear')
jugador2 = raw_input("JUGADOR-2.Introduce que jugada quieres: ")
os.system('clear')

if jugador1 == jugador2 :
	
	print "Empate"
	
if ( jugador1 == "Piedra" and jugador2 == "Tijeras" ) or ( jugador1 == "Tijeras" and jugador2 == "Papel" ) or ( jugador1 == "Papel" and jugador2 == "Piedra" ) :
	
	print "Jugador 1 gana"
	
else :
	
	print "Jugador 2 gana"
