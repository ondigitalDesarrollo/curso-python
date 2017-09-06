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

## SINTAXIS:

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

## Operadores Matemáticos 

* (+) Suma
* (-) Resta
* (asterisco) Multiplicación
* (/) División
* (//) División de enteros
* (%) Operador de módulo
* (doble asterisco) Potencias
* (>) Mayor que
* (<) Menor que
* (==) Igual
* (>=) Mayor igual
* (<=) Menor igual


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


## Condicionales

### If

Los condicionales tienen la siguiente estructura. Ten en cuenta que lo que contiene los paréntesis es la comparación que debe cumplir para que los elementos se cumplan.

### Bucle FOR

El bucle de for lo puedes usar de la siguiente forma: recorres una cadena o lista a la cual va a tomar el elemento en cuestión con la siguiente estructura:

    for i in ____:
 	    elementos

    for i in range(10):
        print i

En este caso recorrerá una lista de diez elementos, es decir el _print i _de ejecutar diez veces. Ahora i va a tomar cada valor de la lista, entonces este for imprimirá los números del 0 al 9 (recordar que en un range vas hasta el número puesto -1).

### Bucle While

En este caso while tiene una condición que determina hasta cuándo se ejecutará. O sea que dejará de ejecutarse en el momento en que la condición deje de ser cierta. La estructura de un while es la siguiente:

    while (condición):
        elementos



## Conceptos Básicos

### Orden de Operaciones

_PEMDAS (ParentesisExponentesMultiplicaciónDivisiónAdiciónSustracción)_

* Paréntesis
* Exponentes
* Multiplicación/División
* Adición/Sustracción

### Valores y Tipos

Los valores son uno de los componentes básicos con los que trabaja un programa, como una letra o un un número, todos los valores tienen un tipo.

Los tipos le permiten a Python saber cuál es el resultado de aplicar determinada operación, los tipos básicos son:

* Integer <int>
* Float <float>
* String <str>
* Boolean <bool>

Para saber el tipo de valor usamos la función type(2)

### Declarar Variables y Expresiones

Las variables nos permiten guardar valores, permitiéndonos reutilizarlos en diferentes partes del código y haciendo nuestros programas más legibles.El valor que contiene una variable puede ser reasignado, significa que podemos asignarle diferentes valores a una misma variable.

Las variables tienen algunas limitantes, por ejemplo:

* Tienen que tener un nombre significativo, es decir, que nos digan qué están haciendo.
* No podemos usar palabras reservadas del lenguaje como nombres para nuestras variables (por ejemplo class, false, none, true).

#### Nombres de Variables:

* Tienen que tener un nombre significativo
* Relacionados con lo que representa la variable
* No deben ser Keywords (Palabaras Reservadas)

*Recuerda:*

* Todos los programas de Python deben guardarse con extensión .py
* Para darle soporte a acentos en nuestros programas debemos usar la línea # -- coding: utf-8 -*-

### Funciones

Las funciones son un concepto fundamental en programación, una función es una secuencia de comandos que realizan un computo.
En Python las funciones se definen usando la palabra reservada def y luego el nombre de la función con paréntesis y dos puntos que indican que lo que sigue son los comandos, una función debe retornar un valor, para esto se usa la palabra reservada return.

*Recuerda:*

* Si usas Python 3, debes usar la función input() para recibir datos del usuario.
* Para definir dónde comenzar el código usamos la línea Screen Shot 2017-08-17 at 4.42.46 PM.png
* Para definir un bloque dentro de la función debemos indentar con 4 espacios.
* Las funciones nos permiten ejecutar determinado código con diferentes valores.

### Funciones con Parámetros

**Limites al declarar funciones**

* EL nombre de la función no puede empezar como un digito.
* No pueden utilizar una palabra reservada.
* Las variables deben tener nombres diferentes.
* Los nombres de las funciones deben ser descriptivas de lo que hacen las funciones.

### Condicionales

* Una expresión booleana se evalúa como verdadera o falsa (True, False)
Podemos utilizar:

#### Operadores relacionales:

* == Es igual
* != Es diferente
* > Es mayor
* >= Es mayor o igual
* < Es menor
* <= Es menor o igual


#### Operadores Lógicos:

* and
* or
* not

## Buenas Prácticas del Lenguaje

### Zen de Python

Hermoso es mejor que feo.
Explícito es mejor que implícito.
Simple es mejor que complejo.
Complejo es mejor que complicado.
Sencillo es mejor que anidado.
Escaso es mejor que denso.
La legibilidad cuenta.
Los casos especiales no son lo suficientemente especiales para romper las reglas.
Lo práctico le gana a la pureza.
Los errores no debe pasar en silencio.
A menos que sean silenciados.
En cara a la ambigüedad, rechazar la tentación de adivinar.
Debe haber una - y preferiblemente sólo una - manera obvia de hacerlo.
Aunque esa manera puede no ser obvia en un primer momento a menos que seas holandés.
Ahora es mejor que nunca.
Aunque “nunca” es a menudo mejor que “ahora mismo”.
Si la aplicación es difícil de explicar, es una mala idea.
Si la aplicación es fácil de explicar, puede ser una buena idea.
Los espacios de nombres son una gran idea ¡hay que hacer más de eso!


## Comparación de strings y unicode

Los *strings* tiene una característica muy importante: son inmutables, esto quiere decir que no se pueden cambiar después de que se han declarado.
Si quieres modificar el texto de un *string* debes definir un nuevo string y modificarlo usando funciones como *slice.*

**Comparación de Strings**

Se pueden realizar operaciones con strings, por ejemplo comparar si son iguales o mayores o menores.

**Diferencia entre ASCII y Unicode**

Los caracteres también son números, para esto existen estándares que asigna un número a cada carácter, para generar un estándar se creó el ASCII pero esta solo toma en cuenta los caracteres en inglés, para dar soporte a más lenguajes se crea UNICODE.

Python codifica en ASCII por default, para cambiarlo por UNICODE debemos colocar u antes del string.

* Ambos sin codificadores de lenguaje
* ASCII (American Standard Code For Information Interchange*
* UNICODE incluye la mayoria de los abecedarios


## Factorial 

Este paradigma busca resolver los problemas metiéndose en otro llamado funcional: todo son funciones matemáticas. ¿Qué tiene de distinto esto con lo que venimos viendo? Que en este caso no vamos a usar ciclos, ya que al fin y al cabo se podrían imitar con recursiones ¿no?.
Para que esto tenga sentido y funcione tienen que pasar dos cosas:

* f tiene que tener un “caso base”, es decir, una condición que haga frenar la recursión. Es un conjunto de valores, tales que cuando f los recibe, retornará una respuesta sin volver a realizar recursión.

* f debería tener un “caso recursivo”, es decir, una condición que le haga seguir haciendo recursión (hasta eventualmente - si las cosas están bien hechas - llegar a un caso base y así terminar).

## Manejo de Strings en Python

Un string es una secuencia de caracteres, donde cada caracter tiene un indice que inicia en cero. Para saber la longitud de un string se usa la función len().

    len(my_string)

Para obtener el último caracter del string se usa la siguiente línea de código

    my_string[len(my_string)-4]

### Métodos de los Strings

Existen métodos del lenguaje para manipular el string de manera sencilla.

* upper
* isupper
* lower
* islower
* find
* isdigit
* endswidth
* starswidth
* split
* join

## Separar Cadenas de Texto

La función slice de python nos permite separar los strings en substrings generando nuevas secuencias.

* Se puede obtener una substring utilizando la notación de _slices_
* Se definen los rangos que se requieren y los saltos necesarios.

    my_string = \'platzi \'
    my_string[1:3] # la
    my_string[1:] # latzi
    my_string[1:6:2] # lti
    my_string[::-1] # iztalp    
    my_string[starts:end:steps] # iztalp    

## Iteraciones

### Función Range

La función range nos permite generar un string apartir de un rango.

    range(5) # [0,1,2,3,4]
    range(5, 40, 3)

### Ciclos con For

for nos permite recorrer un arreglo, asignando cada valor a una variable que decidas.

* Se puede usar para recorrer strings
* Se nececita el keyword `in`
* Si se requiere salir de la iteración se utiliza e keyword `break`
* Si se requiere pasar a la siguiente iteración se utiliza e keyword `continue`


### While Loop

* Similar a un `for` loop, pero en lugar de recorrer una secuencia, se ejecuta hasta ue una condición se convierta en falsa.
* Se debe tener mucho cuidado e no caer en un **infinite loop**

    i = 0
    while i > 0
        print('Ando en un loop')
        i -= 1







