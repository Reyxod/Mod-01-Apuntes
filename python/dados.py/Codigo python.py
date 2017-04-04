# !/usr/bin/python
# -*-coding: utf-8-*-

import os
from random import randint

os.system('clear')

dado1jugador = randint(1,6)
dado2jugador = randint(1,6)
dado1maquina = randint(1,6)
dado2maquina = randint(1,6)

jugador = dado1jugador + dado2jugador
maquina = dado1maquina + dado2maquina

if jugador == maquina :

	print "El jugador saca",dado1jugador,"+",dado2jugador,"=",jugador,"y la maquina",dado1maquina,"+",dado2maquina,"=",maquina,"--> Es un empate"
	
elif jugador > maquina :
	
	print "El jugador saca",dado1jugador,"+",dado2jugador,"=",jugador,"y la maquina",dado1maquina,"+",dado2maquina,"=",maquina,"--> El jugador gana"
			
else :

	print "El jugador saca",dado1jugador,"+",dado2jugador,"=",jugador,"y la maquina",dado1maquina,"+",dado2maquina,"=",maquina,"--> La maquina gana"
