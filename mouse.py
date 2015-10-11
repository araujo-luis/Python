import simpleguitk as simplegui
import math
WIDTH = 500
HEIGHT = 500
BALL_RADIUS = 15
ball_pos = [WIDTH/2, HEIGHT/2]
color = "red"

def distancia(p,q):
    return math.sqrt( (p[0] - q[0])**2 + (p[1]- q[1])**2)
def click(pos):
    #esta funcion recibe un parametro, el cual es la posicion (tupla) de donde hago click
    global ball_pos, color
    if distancia(pos, ball_pos) < BALL_RADIUS:
        color= "green"
    else:
        ball_pos = list(pos)
        #la convierto a lista en lugar de tupla, pues la tupla es inmutable
        color = "red"


def draw(canvas):
    canvas.draw_circle(ball_pos, BALL_RADIUS,1, "black", color)

marco = simplegui.create_frame("Seleccion con Mouse", WIDTH, HEIGHT)

marco.set_canvas_background("White")

marco.set_draw_handler(draw)
#manejdor del mouse cuando hace click, y llama a la funcion click
marco.set_mouseclick_handler(click)
marco.start()
