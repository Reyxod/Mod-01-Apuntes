# !/usr/bin/python
# -*-coding: utf-8-*-
##############################################
#          Llegim la taula "pedidos"         #
##############################################

import os
import sys
import string
import psycopg2    # CAl fer "dnf -y install python-psycopg2"


##############################################
#          Ens connectem a la BBDD           #
##############################################
try:
	conn = psycopg2.connect(database="training", user="postgres", password="jupiter")
	print "DATABASE OPENED SUCCESSFULLY \n"
	
except:
	print "CONNECTION ERROR"
	exit(2)



##############################################
#            Declarem el cursor              #
##############################################
cur = conn.cursor()

os.system('clear')
sortir = False

##############################################
#              Menu principal                #
##############################################
while sortir == False:	
	
	os.system('clear')
	print "OPCIONS \n \n 1- Llegir nom taula: \n 0- Sortir \n"

	opcio = raw_input('Escull una opció [0-1]: ')
	
    # Comprovem si l'opció és correcta
	if not opcio.isdigit() or not ( int(opcio) >= 0 and int(opcio) <= 1 ):
		os.system('clear')
		print "Opció incorrecta, torna a provar \n"
		tecla = raw_input('Prem una tecla per continuar')

	else:
		opcio = int(opcio)

    # Sortim
	if opcio == 0:
		print "Adeu! \n"
		sortir = True

	# Llegim la taula "clientes"
	elif opcio == 1: 
		
		os.system('clear')
		
		try:	
				nombretabla = raw_input ("Indica nombre de tabla : ")
				sql = "select * from " + nombretabla
				cur.execute(sql);
				rows = cur.fetchall()
				
				os.system('clear')
				
				if nombretabla == "pedidos":
					
					print "num_pedido | fecha_pedido | clie | rep | fab | producto | cant | importe"
					
					
					for row in rows:
					   
						print(" {:^10}   {}   {:^6} {:^5} {:^5} {:^10} {:^6} {:^10} ".format(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7]))
					
					tecla = raw_input('Prem una tecla per continuar')
					
				elif nombretabla == "clientes":
					
					print "NUM_CLIE         EMPRESA         REP_CLIE  LIMITE_CREDITO "
					
					
					for row in rows:
						
						print(" {:^10} {:^20} {:^10} {:^10} ".format(row[0], row[1], row[2], row[3]))
				
					tecla = raw_input('Prem una tecla per continuar')
		
		except psycopg2.Error as er :
			print "-------- ERROR:", er.pgcode, " -------- \n"
			conn.rollback()

##############################################
#        Ens desconnectem de la BBDD         #
##############################################
conn.close()
