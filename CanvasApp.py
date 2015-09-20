"""
Aplicacion interactiva que muestra la cantidad de dinero ingresada
y los centavos en el canvas
"""
import simpleguitk as simplegui

dinero = 3.14
def convertir_unidades(valor, nombre):
    cadena = str(valor) +" "+ nombre
    if valor>1:
        cadena = cadena + "s"
    return cadena

def convertir(valor):
    dinero = int(valor)
    centavos = round( 100* (valor - int(valor)) )

    str_dinero = convertir_unidades(dinero, "Lempira")
    str_centavos = convertir_unidades(centavos, "Centavo")

    if dinero == 0 and centavos ==0:
        return "Broke"
    elif dinero == 0:
        return str_centavos
    elif centavos == 0:
        return str_dinero
    else:
        return str_dinero + " y "+ str_centavos

def get_dinero(valor):
    global dinero
    dinero= float(valor)


def dibujar(canvas):
    global dinero
    canvas.draw_text(convertir(dinero), [10,110],24, "white")


marco = simplegui.create_frame("Dinero", 400,200)
marco.add_input("Ingresa cantidad de dinero: ",get_dinero, 100)
marco.set_draw_handler(dibujar)
marco.start()
