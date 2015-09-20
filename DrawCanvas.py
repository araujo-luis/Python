import simpleguitk as simplegui

#Funcion que hace de controlador de dibujo draw_handler
#el parametro es el 'canvas', osea lo que quiero que muestre en la pantalla

def dibujo(contenido):
    #son algunas funcion que tiene para dibujar formas, o escribir texto
    #draw_text(text, [width, height], font-size, color )
    contenido.draw_text("Luis Araujo", [100,100],24,"white")

    #draw_circle([width, height], radio, anchor, line-color,inside-color )
    contenido.draw_circle([100,100],10,1,"red", "white")

marco = simplegui.create_frame("Canvas",300,200)
marco.set_draw_handler(dibujo)
marco.start()
