 # -- coding: utf-8 -*-


def change_calculator(ammount):
    mex_to_col_rate = 145.97
    return mex_to_col_rate * ammount


def run():
    print ('Calculadora de Divisas')
    print ('Convierte Pesos Mexicanos a Pesos Colombianos')
    print ('')


    ammount = float(raw_input('Ingresa la cantidad de pesos mexicanos a convertir: '))

    result = change_calculator(ammount)
    
    print('${} pesos mexicanos son  ${} pesos colombianos'.format(ammount,result))
    print('')

if __name__ == '__main__':
    run()