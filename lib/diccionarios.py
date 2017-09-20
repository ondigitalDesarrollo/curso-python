# -*- coding: utf-8 -*- 

calificaciones = {}

calificaciones['algoritmos'] = 9;
calificaciones['matematicas'] = 7;
calificaciones['Lógica'] = 6;
calificaciones['redacción'] = 6;

suma_de_calificaciones = 0

for key, value in calificaciones.items():
    print('materia: {} calificación: {}'.format(key, value))
    suma_de_calificaciones += value
    print(suma_de_calificaciones)
promedio=float (suma_de_calificaciones/len(calificaciones.values()))
print(promedio)