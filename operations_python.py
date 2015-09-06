# aritmetica modular , Modulos en python
#Aritmetica Modular
#Sacar las decenas y unidades de numeros

num = 83
decenas= num//10 #esto signo '//' es integer division, obtiene la parte entera de la division
unidades=num%10
print (num)
print("Decenas: " +str(decenas) + " Unidades: " + str(unidades))


#Aritmetica del reloj
hora = 20
sumatoria  = 8
hora_resultante = (hora +sumatoria) % 24

#Aritmetica de limite de posicionamiento
#en pixeles, suponiendo que el limite es 800, asi que debe regresar al inicio
ancho = 800
posicion_actual = 797
movimiento = 5
posicion_nueva = (posicion_actual + movimiento) % ancho
print (posicion_nueva)
#la posicion nueva seria 2 pixeles desde el inicio


#converir una la hora al reloj de 24hrs

hora = 5
unidades = hora % 24
decenas = 5//10
print(  str(decenas)+ str(unidades)+":00")


"""Modulos en Python, son como librerias que contienen funciones que
son muy utiles, y que ya estan hechas.
Por lo tanto haya que importarlas 'import'
"""

import math
import random

print( math.pi)
