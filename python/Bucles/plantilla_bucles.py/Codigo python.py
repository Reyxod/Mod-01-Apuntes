# !/usr/bin/python
# -*-coding: utf-8-*-

import os

salir = False

while salir == False :
	
	os.system('clear')
	print "Hola\n"
	tecla = raw_input ("Si quieres salir pulsa s o S: ")
	os.system('clear')
	
	if ( tecla == "s" ) or ( tecla == "S" ) :
		
		print "Adios"
		salir = True
		
	else :
		
		print "Esta opcion no esta contemplada\n"
		tecla = raw_input("Pulsa enter para volver a intentar")
