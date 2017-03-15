# !/usr/bin/python
# -*-coding: utf-8-*-

import os

os.system('clear')

mano_der = "movil"
mano_izq = "bocadillo"

print "En la mano derecha tengo un:",mano_der
print "En la mano izquierda tengo un:",mano_izq,"\n \nLas intercambio y ahora:\n"

mano_extra = mano_der
mano_der = mano_izq
mano_izq = mano_extra

print "En la mano derecha tengo un:",mano_der
print "En la mano izquierda tengo un:",mano_izq
