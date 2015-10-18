#PROGRAMACION ORIENTADA A OBJETOS EN PYTHON

class Character:
    #__init__ es el constructor, importante el objeto "self" es objeto y no variable
    #las variables del constructor son name e initial_health
    #self es lo mismo que "this" en C# o "me" en VB.NET
    def __init__(self, name, initial_health):
        self.name = name
        self.health = initial_health
        self.inventory = []

    # __str__ es otra funcion especial, viene siento el toString() en VB.NET
    #y puedo acceder a las propiedades name, health, y tambien inventory
    def __str__(self):
        s  = "Name: " + self.name
        s += ", Health: " + str(self.health)
        s += ", Inventory: " + str(self.inventory)
        return s

    #funciones normales
    def grab(self, item):
        self.inventory.append(item)

    def get_health(self):
        return self.health

#ojo, no se pasa el parametro self, y se ejecuta el constructor
yo = Character("Luis", 21)

#cuando imprimo el objeto se llama el metodo __str__
print (yo)

#puedo llamar a mas funciones
yo.grab("pc")
yo.grab("telefono")

print (yo)
print (yo.get_health())
