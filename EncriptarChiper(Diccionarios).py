

import simpleguitk as simplegui

import random
CIPHER = {}

message = ""

LETRAS = "abcdefghijklmnopqrstuvwxyz";

def inicializacion():
    #Convierte el string LETRAS A una lista
    lista_letras = list(LETRAS)
    #coloca las letras en un orden aleatorio
    random.shuffle(lista_letras)
    print(lista_letras)
    for ch in LETRAS:
        CIPHER[ch] = lista_letras.pop()
        print(CIPHER[ch])

    print (lista_letras)



# Encode button
def encode():
    emsg = ""
    for ch in message:
        emsg += CIPHER[ch]

    print (message, "encodes to", emsg)

# Decode button
def decode():
    dmsg = ""
    for ch in message:
        """la funcion items devuelve uns lista de pares ordenados de (llave,valor), por ejemplo
            {1: 'a', 2: 'b', 3: 'c'}.items()   devuelve  [(1, 'a'), (2, 'b'), (3, 'c')]
            y por cada item, almacena la llave en key, y el valor en value
        """
        for key, value in CIPHER.items():
            if ch == value:
                dmsg += key
    print (message, "decodes to", dmsg)

# Update message input
def newmsg(msg):
    global message
    message = msg
    label.set_text(msg)

# Create a frame and assign callbacks to event handlers
frame = simplegui.create_frame("Cipher", 2, 200, 200)
frame.add_input("Message:", newmsg, 200)
label = frame.add_label("")
frame.add_button("Encode", encode)
frame.add_button("Decode", decode)
inicializacion()
# Start the frame animation
frame.start()
