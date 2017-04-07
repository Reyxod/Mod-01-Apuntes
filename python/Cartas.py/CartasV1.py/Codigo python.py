# !/usr/bin/python
# -*-coding: utf-8-*-

import os
from random import randint

os.system('clear')

palo = {1:"Corazones",2:"Trevoles",3:"Picas",4:"Diamantes"}
carta = {2:"2",3:"3",4:"4",5:"5",6:"6",7:"7",8:"8",9:"9",10:"10",11:"J",12:"Q",13:"K",14:"A"}

jcarta = randint(2,14)
jpalo = randint(1,4)
mcarta = randint(2,14)
mpalo = randint(1,4)
jugador = carta[jcarta]+" de "+palo[jpalo]
maquina = carta[mcarta]+" de "+palo[mpalo]

if jcarta == mcarta :
	
	print "El jugador ha sacado",jugador,"y la maquina",maquina," --> Es un empate"
	
elif jcarta > mcarta :
	
	print "El jugador ha sacado",jugador,"y la maquina",maquina," --> El jugador gana"

else :
	
	print "El jugador ha sacado",jugador,"y la maquina",maquina," --> La maquina gana"
