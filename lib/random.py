# -*- coding: utf-8 -*-

import random

def run():
    number_found = False
    max_number = int(input('Elige el número máximo: '))
    random_number = random.randint(0,max_number)

    while not number_found:
        number = int(input('Intenta un número: '))

        if number == random_number:
            print('Felicidades, encontraste el número')
            number_found=True
        elif number > random_number:
            print('El número es más pequeño')
        else:
            print('El número es más grande')


if __name__ == '__main__':
    run()