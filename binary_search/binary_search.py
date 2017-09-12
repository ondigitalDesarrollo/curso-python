# -*- coding: utf-8 -*-

def binary_search(numbers, number_to_find, low, hight):
    if low > hight:
        return False

    mid = low + hight / 2

    if numbers[mid] == number_to_find:
        return True
    elif numbers[mid] > number_to_find:
        return binary_search(numbers, number_to_find,low, hight - 1)
    else:
        return binary_search(numbers, number_to_find,mid + 1, hight)
        
        
    

if __name__ == '__main__':
    numbers = [1,3,4,5,6,8,10,11,25,28,29,34,36,49]

    number_to_find = int(raw_input('Ingresa un número: '))

    result = binary_search(numbers, number_to_find,0,len(numbers) - 1)

    if result == True:
        print('El numero si esta en la lista')
    else:
        print('El numero no esta en la lista')
        