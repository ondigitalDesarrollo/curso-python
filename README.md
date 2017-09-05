# PYTHON

Python es un lenguaje bastante bueno para aprender a programar ya que tiene una comunidad muy grande que te ayudará a superar tus dudas, tiene una sintaxis para escribir bastante sencilla.

## ¿QUÉ ES PROGRAMAR?

La programación es dar instrucciones a la computadora de forma ordenada, estas instrucciones definen lo que se va a realizar, desde cosas sencillas hasta cosas avanzadas.
Todos los programas se componen de partes esenciales que son forma de darle datos de entrada a la computadora y formas estructuradas para procesar estos datos.

## ¿Qué es Python?

> Python es un lenguaje de programación creado por Guido Van Rossum, con una sintaxis muy limpia, ideado para enseñar a la gente a programar     bien. Se trata de un lenguaje interpretado o de script.

## Ventajas:

* Legible: sintaxis intuitiva y estricta.
* Productivo: ahorra mucho código.
* Portable: para todo sistema operativo.
* Recargado: viene con muchas librerías por defecto.

## Lo Básico:

### Tipos de Datos

* Enteros (int): En este grupo en este grupo están todos los números, enteros y long.

    *ejemplo: 1, 2.3, 2121, 2192, -123*

* Booleanos (bool): Son los valores falso o verdadero, compatibles con todas las operaciones booleanas ( and, not, or ).

    *ejemplo: True, False*

* Cadenas (str): Son una cadena de texto.

    *ejemplos: “Hola”, “¿Cómo estas?”*

* Listas: Son un grupo o array de datos, puede contener cualquiera de los datos anteriores.

    *ejemplos: [1,2,3, ”hola” , [1,2,3] ], [1,“Hola”,True ]*

* Diccionarios: Son un grupo de datos que se acceden a partir de una clave.

    *ejemplo: {“clave”:”valor”}, {“nombre”:”Fernando”}*

* Tuplas: también son un grupo de datos igual que una lista con la diferencia que una tupla después de creada no se puede modificar.

    *ejemplos: [1,2,3, ”hola” , [1,2,3] ], [1,“Hola”,True ] (Pero jamás podremos cambiar los elementos dentro de esa Tupla)*

En Python trabajas con módulos y ficheros que usas para importar las librerías.

### Funciones

Las funciones las defines con def junto a un nombre y unos paréntesis que reciben los parámetros a usar. Terminas con dos puntos.

def nombre_de_la_función(parametros):

Después por indentación colocas los datos que se ejecutarán desde la función:

    >>> def my_first_function():
    ...	return “Hello World!” 
    ...    
    >>> my_first_function(

### Variables

Las variables, a diferencia de los demás lenguajes de programación, no debes definirlas, ni tampoco su tipo de dato, ya que al momento de iterarlas se identificará su tipo. Recuerda que en Python todo es un objeto.

    A = 3
    B = A

### Listas

Las listas las declaras con corchetes. Estas pueden tener una lista dentro o cualquier tipo de dato.

    L = [22, True, "una lista", [1,2]]
    L[0]

### Tuplas

Las tuplas se declaran con paréntesis, recuerda que no puedes editar los datos de una tupla después de que la has creado.

    T = (22, True, "una tupla", (1, 2)) 
    T[0] 

### Diccionarios

En los diccionarios tienes un grupo de datos con un formato: la primera cadena o número será la clave para acceder al segundo dato, el segundo dato será el dato al cual accederás con la llave. Recuerda que los diccionarios son listas de llave:valor.

    D = {"Kill Bill": "Tamarino", "Amelie": "Jean-Pierre- Jeunet"}


### Conversiones

De Flotante a Entero:

    int(4.3)

De Entero a Flotante:

    float(4)

De Entero a String:

    str(4.3)

De Tupla a Lista:

    list(4,5,6)


## Operadores Comunes

Longitud de una cadena, lista, tupla, etc.:

     len("key")

Tipo de dato:

    type(4) 

Aplicar una conversión a un conjunto como una lista:

    map(str, [1, 2, 3, 4])

Redondear un flotante con x número de decimales:

    round(6.3243, 1)

Generar un rango en una lista (esto es mágico):

    range(5)

Sumar un conjunto:

    sum([1, 2, 4])

Organizar un conjunto:

    sorted([5, 2, 1])

Conocer los comandos que le puedes aplicar a x tipo de datos:

    Li = [5, 2, 1]
    dir(Li)

‘append’, ‘count’, ‘extend’, ‘index’, ‘insert’, ‘pop’, ‘remove’, ‘reverse’, ‘sort’ son posibles comandos que puedes aplicar a una lista.

Información sobre una función o librería:

    help(sorted)

## Clases

Clases es uno de los conceptos con más definiciones en la programación, pero en resumen sólo son la representación de un objeto. Para definir la clase usas_ class_ y el nombre. En caso de tener parámetros los pones entre paréntesis.

Para crear un constructor haces una función dentro de la clase con el nombre init y de parámetros self (significa su clase misma), nombre_r y edad_r:

    class Estudiante(object):
        def __init__(self, nombre_r, edad_r):
            self.nombre_r = nombre_r
            self.edad_r = edad_r
        def hola(self):
            return "Mi nombre es %s y tengo %i " % (self.nombre_r,self.edad_r)

    e = Estudiante("Arnold", 23)
    print e.hola()

## Métodos Especiales

_cmp(self,otro)_
Método llamado cuando utilizas los operadores de comparación para comprobar si tu objeto es menor, mayor o igual al objeto pasado como parámetro.

_len(self)_
Método llamado para comprobar la longitud del objeto. Lo usas, por ejemplo, cuando llamas la función len(obj) sobre nuestro código. Como es de suponer el método te debe devolver la longitud del objeto.

_init(self,otro)_
Es un constructor de nuestra clase, es decir, es un “método especial” que es llamas automáticamente cuando creas un objeto.





