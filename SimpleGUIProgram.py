#importamos el modulo de simpleguitk para Python3.0
import simpleguitk as simplegui

#definir variables globales

contador = 0

#funciones de ayuda a los controladores de ventos

def incrementar():
    global contador
    contador = contador +1

#definir los manejadores de eventos
def tick():
    incrementar()

def button_press():
    global contador
    contador=0
def mostrar(texto):
    tick()
    texto.draw_text(contador,[50,50],10,"Red")

#Crear el marco(frame)
    #create_frame funcion que pertenece al modulo simplegui

    #sintaxis create_frame('titulo del marco', ancho (weight), largo(height))
marco = simplegui.create_frame("Primer Programa con SimpleGUI", 100,100)

#registrar los manejadores de eventos
temporizador = simplegui.create_timer(1000,mostrar)
marco.add_button("Resetear Contador", button_press)
marco.set_draw_handler(mostrar)

#comenzar los timers y frames
marco.start()
#temporizador.start()
