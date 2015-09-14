#importar solo simplegui para CodeSkulptor
#import simplegui

#importar para usar con  python3.0
import simpleguitk as simplegui

def tick():
    print ("tick!")


timer = simplegui.create_timer(1000, tick)

# Start timer
timer.start()
