#todo lo que quede con sangria forma parte del if
if 20==20:
    print("20 es igual a 20")
    print("asd")

#definicion de una funcion
"""importante las sangrias, todo lo que forma parte de la sangria, es la funcion
y tambien la del if
 """
def funcion(numero):
    if numero==20:
        return "True, numero es igual a 20"
    if numero!=20:
        return "False, numero es distinto de 20"

#llamado de funcion

print (funcion(2))


#if/else
numero = 20

if numero == 1:
    print ("Numero es igual a 1")
else:
    print ("Numero no es igual a 1")


#elseif

numero = 3

if numero==1:
    print("Numero es igual a 1")
elif numero==2:
    print("Numero es igual a 2")
elif numero==3:
    print("Numero es igual a 3")
else:
    print ("Numero no ni 1 ni 2 ni 3")
