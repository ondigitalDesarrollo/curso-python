 # -- coding: utf-8 -*-

import turtle

def main():
    window = turtle.Screen()
    Arnold = turtle.Turtle()

    make_square(Arnold)

    turtle.mainloop()

def make_square(Arnold):
    lenght = int(raw_input('Ingresa el número de pasos: '))
    for i in range(4):
        make_line_and_turn(Arnold, lenght)
        

def make_line_and_turn(Arnold, lenght):
    Arnold.forward(lenght)
    Arnold.left(90)
        

if __name__ == '__main__':
    main()