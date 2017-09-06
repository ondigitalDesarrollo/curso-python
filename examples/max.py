# -*- coding: utf-8 -*-

"""
  Programa para Saber que numero es mayor entre 2 
"""


def max(number1,number2):
    if number1 > number2:
        print('{} es mayor que {}'.format(number1,number2))
    else:
        print('{} es mayor que {}'.format(number2,number1))
        
def max_de_tres(number1, number2, number3):
    if number1 > number2 and number1 > number3:
        print('{} es mayor que {} y que {}'.format(number1,number2,number3))
    elif number2 > number1 and number2 > number3:
        print('{} es mayor que {} y que {}'.format(number2,number1,number3))
    else:
        print('{} es mayor que {} y que {}'.format(number3,number1,number2))
        
            
        

if __name__ == '__main__':
    number1 = int(raw_input('Escribe un número: '))
    number2 = int(raw_input('Escribe otro número: '))
    number3 = int(raw_input('Escribe el último número: '))

    # max(number1, number2)
    max_de_tres(number1,number2,number3)