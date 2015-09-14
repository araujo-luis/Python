"""
Variables globales y locales
"""
#variable global
num = 5
print(num)

def miFuncion():
    num=2
    num2 = num + 1
    print(num2)

miFuncion()
print(num)

"""
Modificar una variable global dentro de una funcion
Utilizando la palabra reservada 'global'
"""

print("\nModificando variable global en una funcion")
num = 5
print(num)

def miFuncion():
    global num
    num=2
    num2 = num + 1
    print(num2)

miFuncion()
print(num)
