# template for "Stopwatch: The Game"
import simpleguitk as simplegui
# define global variables
time = 0
centesimas = 0
segundos = 0
minutos = 0
intentos = 0
aciertos = 0

# define helper function format that converts time
def resultados():
    global intentos, aciertos
    return str(aciertos)+ "/" +str(intentos)

def time_helper(minutos, segundos, centesimas):
    a = ""
    b = ""
    c = ""
    d = ""

    a = str(int(minutos))

    if segundos <=9:
        b = "0"
        c = str(int(segundos))
    else:
        b = str(int(segundos/ 10))
        c = str(int(segundos %10))

    d = str(centesimas)

    return a+":"+b+c+"."+d


# in tenths of seconds into formatted string A:BC.D

def format(t):
    global centesimas, segundos, minutos

    segundos = (t /10)
    minutos = segundos / 60
    segundos = segundos%60
    centesimas = t % 10
    return time_helper(minutos,segundos,centesimas)


# define event handlers for buttons; "Start", "Stop", "Reset"
def start():
    timer.start()

def stop():
    global intentos,aciertos
    timer.stop()
    intentos +=1
    if centesimas == 0:
        aciertos+=1


def reset():
    global time , aciertos, intentos
    time = 0
    aciertos = 0
    intentos = 0
    timer.stop()

# define event handler for timer with 0.1 sec interval
def imprimir():
    global time
    time +=1


# define draw handler
def draw(canvas):
    canvas.draw_text(format(time),[60,110],35,"white")
    canvas.draw_text(resultados(), [150,20], 24 , "green")


# create frame
marco = simplegui.create_frame("StopWatch", 200,200)
marco.add_button("Start", start, 100)
marco.add_button("Stop", stop, 100)
marco.add_button("Reset", reset, 100)

marco.set_draw_handler(draw)
# register event handlers
timer = simplegui.create_timer(100,imprimir)

# start frame
marco.start()
