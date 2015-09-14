import simpleguitk as simplegui

#variables globales
almacen = 0
operador = 0

#funciones de ayuda

def mostrar():
    global almacen,operador
    print("Almacen: " +str(almacen))
    print("Operador: " +str(operador))
    print()


def invertir():
    """Invertimos almacen por operador y viceversa """
    global almacen,operador
    almacen1= almacen
    almacen= operador
    operador =almacen1
    #otra forma de hacerlo
    #almacen, operador = operador, almacen
    mostrar()

def sumar():
    global almacen, operador
    almacen = almacen + operador
    mostrar()

def restar():
    global almacen, operador
    almacen = almacen - operador
    mostrar()

def ingresar(value):
    global operador
    #todo lo que ingresamos por el teclado viene como texto, hay que pasarlo a entero
    operador = float(value)
    mostrar()

"""
LOS RESULTADOS SE VEN EN LA CONSOLA
"""
marco = simplegui.create_frame("Calculadora",300,300)
#EL 100 ES EL ANCHO DEL BOTON
marco.add_button("Mostrar", mostrar, 100)
marco.add_button("Invertir", invertir , 100)
marco.add_button("Sumar", sumar , 100)
marco.add_button("Restar", restar , 100)
marco.add_input("Ingresar operando: ", ingresar,100)

marco.start()
mostrar()
invertir()
