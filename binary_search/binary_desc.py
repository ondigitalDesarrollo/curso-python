# # -*- coding: utf-8 -*-


# def order_list(disorder_list):
#     split_list = map(int, disorder_list.split(' '))
#     order_list = sorted(split_list)
#     return order_list

# def binary_search(order_numbers, number_to_find, low, hight):
#     if low > hight:
#         return False

#     mid = low + hight / 2

#     if order_numbers[mid] == number_to_find:
#         return True
#     elif order_numbers[mid] > number_to_find:
#         return binary_search(order_numbers, number_to_find,low, hight - 1)
#     else:
#         return binary_search(order_numbers, number_to_find,mid + 1, hight)

# if __name__ == '__main__':
   
#     # Capturo la Lista Desordenada
#     disorder_list = str(raw_input('Escribe una lista de 10 números desordenados separados por espacios:'))

#     # Capturo el numero a buscar
#     number_to_find = int(raw_input('Escribe el número para buscar: '))
    
#     # Variables Iniciales
#     order_numbers = order_list(disorder_list)
#     low = 0
#     hight = len(order_numbers) - 1
   
#     # Corro la función principal
#     result = binary_search(order_numbers, number_to_find, low, hight)

#     if result is True:
#         print ('El número sí esta en la lista.')
#     else:
#         print('El número NO esta en la lista.')

# -*- coding: utf-8 -*-
"""binary_search.py"""


def str_2_list(disorder_list):
    split_list = map(int, disorder_list.split(' '))
    order_list = sorted(split_list)

    return order_list


def bynary_search(order_numbers, number_to_find, low, high):
    if low > high:
        return False

    mid = (low + high) / 2

    if order_numbers[mid] == number_to_find:
        return True
    elif order_numbers[mid] > number_to_find:
        return bynary_search(order_numbers, number_to_find, low, mid - 1)
    else:
        return bynary_search(order_numbers, number_to_find, mid + 1, high)


if __name__ == '__main__':
    disorder_list = str(raw_input('Escribe una lista de numeros --AL MENOS DIEZ NUMEROS-- separados por <<ESPACIOS>>: '))
    order_numbers = str_2_list(disorder_list)
    number_to_find = int(raw_input('Ingresa un número a buscar: '))

    result = bynary_search(order_numbers, number_to_find, 0, len(order_numbers) - 1)

    if result is True:
        print('El numero sí esta en la lista')
    else:
        print('El numero NO esta en la lista')
