# import turtle

# window = turtle.Screen()
# Arnold = turtle.Turtle()


# Arnold.forward(50)
# Arnold.left(90)
# Arnold.forward(50)
# Arnold.left(90)
# Arnold.forward(50)
# Arnold.left(90)
# Arnold.forward(50)
# Arnold.left(90)
# Arnold.forward(50)
# Arnold.left(90)

# turtle.mainloop()

def myFunction():
    print 'Hello World'

myFunction()

class Estudiante(object):
    def __init__(self, nombre_r, edad_r):
        self.nombre_r = nombre_r
        self.edad_r = edad_r
    def hola(self):
        return "Mi nombre es %s y tengo %i " % (self.nombre_r,self.edad_r)

e = Estudiante("Arnold", 23)
print e.hola()

        
        