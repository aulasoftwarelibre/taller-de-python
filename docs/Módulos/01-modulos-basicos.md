# Módulos básicos


Python es un lenguaje que viene con "pilas incluidas": la librería estándar del intérprete incluye de serie multitud de *módulos*.

A continuación se comentan algunos de estos módulos que te ayudarán a realizar operaciones complejas de manera inmediata.

## Operaciones matemáticas: `math`

[Documentación](https://docs.python.org/3/library/math.html)

Las operaciones matemáticas es una de las funcionalidades más básicas de cualquier lenguaje de programación. En Python las puedes encontrar en el módulo `math`.

```python
import math
```

Aquí están definidas algunas de las constantes fundamentales:
```python
math.pi
# >> 3.141592653589793
math.e
# >> 2.718281828459045
```

También tenemos acceso a funciones de uso común, como raíces y logaritmos:
```python
math.sqrt(2) # Raíz cuadrada
# >> 1.4142135623730951
math.log(5) # Logaritmo natural (base e)
# >> 1.6094379124341003
```

Python también nos permite trabajar con ángulos fácilmente:
```python
math.sin(math.pi / 2) # Función seno
# >> 1.0
math.cosh(2) # Función coseno hiperbólico
# >> 3.7621956910836314
math.radians(30) # Pasar de grados a radianes
# >> 0.5235987755982988 (~ pi/6)
```

Por último, algunas funciones misceláneas que podrían ser de utilidad:
```python
math.gcd(12, 34) # Máximo común divisor
# >> 2
math.prod([3, 5, 7]) # Productorio
# >> 105 (3 * 5 * 7)
math.factorial(7) # Factorial
# >> 5040
```

Por último mencionar que, de base, también podemos trabajar con datos numéricos muy potentes:
```python
# Enteros de tamaño arbitrario por defecto!:
12381247283945723895734818913812 * 6788678456749293283420582137
# >> 84052306704208035914529211542310875743692802848875069776244

# Números complejos (usamos j en lugar de i):
(3+4j) * (7+10j)
# >> (-19+58j)

# Fracciones
from fractions import fraction
Fraction(10,9) / Fraction(7,8)
# >> Fraction(80, 63)
```

## Operaciones sobre cadenas: `str`

Uno de los puntos fuertes de Python es la facilidad del manejo de cadenas. Tenemos mucha flexibilidad para definir cadenas y además disponemos de muchas operaciones sobre ellas:
```python
'escribir En Mayúsuclas y miNúsculas'.capitalize()
# >> 'Escribir en mayúsuclas y minúsculas'

'uno, dos, tres'.split(', ')
# >> ['uno', 'dos', 'tres']

'''Esto es una cadena multilínea.
Puedes escribir saltos de línea entre medias.
Esto es un ejemplo y no se me ocurre qué más poner'''.splitlines()
# >> ['Esto es una cadena multilínea.', 'Puedes escribir saltos de línea entre medias.', 'Esto es un ejemplo y no se me ocurre qué más poner']
```

Si tenemos que construir cadenas a partir de variables en nuestro código tenemos varias formas de hacerlo.

El método original se parece mucho a cómo lo hacemos en C con la función `printf`. Para ello, usamos el operador `%` sobre una cadena.
```python
entero = 3
flotante = 2.1
cadena = 'hola'

'Igual que printf en C, puedes imprimir valores: %d' % entero
# >> 'Igual que printf en C, puedes imprimir valores: 3'

'Puedes poner más de un valor: %d y "%s"' % (entero + 2, cadena)
# >> 'Puedes poner más de un valor: 5 y "hola"'

'Y puedes especificar el formato: %.3f' % flotante
# >> 'Y puedes especificar el formato: 2.100'
```

También podemos usar el método `.format()`, que nos permite mayor flexibilidad en el orden de los parámetros y puede hacer el código más legible.
```python
'Otra forma de formatear es con el método "format": {}'.format(entero)
# >> 'Otra forma de formatear es con el método "format": 3'

'Puedes especificar el orden: {2}, {0}, {1}'.format(entero, flotante, cadena)
# >> 'Puedes especificar el orden: hola, 3, 2.1'

'O incluso llamarlos por su nombre: {n}, {f}, {c}'.format(n=entero+1, f=flotante*2, c=cadena)
# >> 'O incluso llamarlos por su nombre: 4, 4.2, hola'
```

Por último, desde la versión 3.6, podemos integrar las propias expresiones dentro de la cadena usando lo que se denomina "f-strings":
```python
f'A partir de Python 3.6 puedes usar "f-strings": {entero + 1}, {flotante * 2:.3f}, {cadena}'
# >> 'A partir de Python 3.6 puedes usar "f-strings": 4, 4.200, hola'
```

!!! tip "Consejo"
    Ahí fuera encontrarás programas que utilizan cualquier combinación de los tres métodos anteriores (siempre el mismo o mezclados). Nuestro consejo es que, siguiendo los principio de "código limpio", *trates de adherirte a un sólo método dentro del mismo repositorio de código* para facilitar la lectura.
    
    Si se trata de código desde cero y se usa una versión compatible, *recomendamos usar los f-string* por ser generalmente más legibles y cómodos.
    
    Eso sí, en situaciones concretas podría tener más sentido usar uno sobre los demás. ¡Piensa bien lo que haces y ponte en el lugar de alguien leyendo tu código!

## Copiado de objetos: `copy`

[Documentación](https://docs.python.org/3/library/copy.html)

En Python, por defecto, todos los valores son *referencias* a un objeto. Si copiamos una referencia a un objeto *mutable* (es decir, que puede ser modificado), por ejemplo una lista, ambas copias se refieren a la misma lista. Por ejemplo:
```python
a = ['hola', 'adios', 'buenas']
b = a  # Copiamos la referencia, NO SE HACE COPIA
b[0] = 'hastaluego'  # Estamos modificando la lista original
print(a)
# >> ['hastaluego', 'adios', 'buenas']
print(b)
# >> ['hastaluego', 'adios', 'buenas']
```

Si, por algún motivo, necesitamos tener copias independientes, podemos hacer copias usando el módulo `copy`:
```python
import copy

a = ['hola', 'adios', 'buenas']
b = copy.copy(a)  # Creamos una copia de la lista
b[0] = 'hastaluego'  # Estamos modificando la copia
print(a)
# >> ['hola', 'adios', 'buenas']
print(b)
# >> ['hastaluego', 'adios', 'buenas']
```

¡Mucho ojo con objetos anidados! En el siguiente ejemplo tenemos una *lista de listas*. Si simplemente copiamos la lista externa, ambas listas contienen referencias a las mismas listas.
```python
a = [[1, 2], [3, 4], [5, 6]]
b = copy.copy(a)  # Copiamos las referencias, pero apunta a las mismas listas
b[0][1] = 10  # Ojo, estamos cambiando la primera lista
print(a)
# >> [[1, 10], [3, 4], [5, 6]]
```

!!! question inline end "Ejercicio"
    Un buen ejercicio para practicar el pensamiento recursivo es implementar una función de copia profunda (equivalente a `copy.deepcopy()`) usando únicamente la función de copia `copy.copy()`. ¡Inténtalo!

Si esto no es lo que queremos, tenemos que hacer una *copia profunda* o "deep copy" (es decir, ¡una copia recursiva!):
```python
a = [[1, 2], [3, 4], [5, 6]]
b = copy.deepcopy(a)
b[0][1] = 10
print(a)
# >> [[1, 2], [3, 4], [5, 6]]
print(b)
# >> [[1, 10], [3, 4], [5, 6]]
```

## Generadores aleatorios: `random`

[Documentación](https://docs.python.org/3/library/random.html)

A veces nuestro programa necesita implementar algún tipo de comportamiento (aparentemente) aleatorio. Python dispone de un montón de utilidades para esto en el módulo `random`.

!!! warning "¡Cuidado!"
    Las funciones que se presentan aquí generan números y secuencias *pseudo*-aleatorias. Estas son muy útiles para situaciones donde algo sólo debe aparentar ser aleatorio (por ejemplo: un efecto gráfico, el daño realizado a un enemigo en un videojuego, una simulación física, etc.).
    
    Para aplicaciones donde **la seguridad de la información esté en juego** (por ejemplo, un algoritmo de cifrado de mensajes secretos, una bajara virtual de póker de un casino online, etc.) el módulo `random` **NO ES ADECUADO**. En esos casos es necesario encontrar una verdadera fuente de aleatoriedad sin sesgos.

Por defecto, al importar `random`, el intérprete toma la "semilla" para generar números aleatorios de una fuente de aleatoriedad del sistema. Nosotros podemos especificar la semilla que queramos si, por ejemplo, queremos que nuestro código sea reproducible. 
    
```python
import random

random.seed(123)
```

Disponemos de varias funciones para generar números aleatorios de distinta índole:
```python
# Generar valores flotantes en el rango [0.0, 1.0)
random.random()
# >> 0.052363598850944326

# Generar valores enteros en el rango [a, b)
random.randrange(8) # Si solo ponemos un argumento, por defecto toma [0, a)
# >> 1

# O si queremos un rango cerrado en ambos extremos [a, b]
random.randint(2, 8)
# >> 8
```

También tenemos múltiples operaciones para obtener elementos aleatorios (*muestras*) de listas:
```python
lista = ['alice', 'bob', 'carol', 'eva']
# Elegir un elemento aleatorio de una lista
random.choice(lista)
# >> eva

# Lo anterior es una manera más compacta de escribir:
lista[random.randrange(len(lista))]
# >> carol

# Elegir varios elementos aletorios de una lista CON REEMPLAZO
# Es decir, pueden salir elementos repetidos
random.choices(lista, k=3)
# >> ['alice', 'eva', 'alice']

# Si no queremos elementos repetidos:
random.sample(lista, 3)
# >> ['carol', 'bob', 'alice']
```

Por último, también podemos desordenar una lista:
```python
lista
# >> ['alice', 'bob', 'carol', 'eva']

# Desordenar la lista
random.shuffle(lista)
lista
# >> ['carol', 'eva', 'alice', 'bob']
```

## Tiempo, fechas y horas: `time`, `datetime`, `calendar`

A menudo necesitamos utilidades para calcular tiempos, horas, fechas, etc. En Python lo tenemos muy fácil gracias a estos tres módulos.

Las funciones del módulo `time` están relacionadas con tiempos de espera y tiempos de cómputo. Por ejemplo, `time.perf_counter()` mide tiempo real, incluyendo tiempo de inactividad. Sólo tiene sentido si calculamos una *diferencia entre dos llamadas*:
```python
import time
import math

inicio = time.perf_counter()  # Empezamos el "cronómetro"

fact = math.factorial(100000)  # Cálculo largo
print(str(fact)[:10])  # Primeros 10 dígitos
# >> 2824229407
fin_factorial = time.perf_counter()  # Fin del cálculo largo
time.sleep(1)  # Ahora un segundo de inactividad

fin = time.perf_counter()  # Paramos el "cronómetro"

print(f'Tiempo de cálculo: {fin_factorial - inicio:.2f} segundos')
print(f'Tiempo total: {fin - inicio:.2f} segundos')
# >> Tiempo de cálculo: 2.38 segundos
# >> Tiempo total: 3.38 segundos
```

Por otro lado, `time.process_time()` mide tiempo *de proceso*, sin incluir el tiempo que el proceso está inactivo (por ejemplo, esperando a que el usuario introduzca algún valor o esperando a algún dispositivo de E/S):
```python
import time
import math

inicio = time.process_time()  # Empezamos el "cronómetro"

fact = math.factorial(100000)  # Cálculo largo
print(str(fact)[:10])  # Primeros 10 dígitos
# >> 2824229407
fin_factorial = time.process_time()  # Fin del cálculo largo
time.sleep(1)  # Ahora un segundo de inactividad

fin = time.process_time()  # Paramos el "cronómetro"

print(f'Tiempo de cálculo: {fin_factorial - inicio:.2f} segundos')
print(f'Tiempo total: {fin - inicio:.2f} segundos')
# >> Tiempo de cálculo: 2.44 segundos
# >> Tiempo total: 2.45 segundos
```

!!! info "Información"
    La pequeña discrepancia en el tiempo de cálculo y tiempo total del último ejemplo se debe a que la propia llamada a `time.sleep(1)`, así como `time.process_time()`, tiene cierta *sobrecarga*.

Podemos usar `datetime` para lidiar con fechas y horas del "mundo real":
```python
from datetime import datetime

# Mi fecha de nacimiento
nacimiento = datetime(1995, 4, 22, 6, 0)
print(nacimiento.weekday())  # ¿Qué día de la semana? (0 = lunes)
# >> 5

# ¿Cuántos años tengo? (datetime - datetime = timedelta)
td = datetime.now() - nacimiento
print(td)
# >> 9473 days, 13:30:38.442574
print(td.days // 365)
# >> 25
print(td.total_seconds())
# >> 818515838.442574
```

Por último `calendar` contiene utilidades relacionadas con calendarios: años bisiestos, nombres de los meses/días de la semana...
```python
import calendar

# Para configurar la localización de fecha/hora a España,
# tenemos que ejecutar lo siguiente:
import locale
locale.setlocale(locale.LC_TIME, 'es_ES.UTF-8')


nombre_dia_semana = calendar.day_name[nacimiento.weekday()]
nombre_dia_mes = calendar.month_name[nacimiento.month]
print(f'Nací un {nombre_dia_semana}, {nacimiento.day} de {nombre_dia_mes} de {nacimiento.year}')
# >> Nací un sábado, 22 de abril de 1995
```

!!! warning "Cuidado"
    Si tu aplicación necesita gestionar más de una localización (p. ej.: español de España y español de México) se desaconseja el uso de `locale.setlocale()`. Este es sólo un pequeño ejemplo.


## Iteradores: `itertools`

En Python llamamos [*iterable*](https://docs.python.org/3/glossary.html#term-iterable) a todo aquel objeto que podemos recorrer mediante un bucle `for`:
```python
for elemento in iterable:
    func(elemento)
```

Esto por supuesto incluye listas (`list`), pero también tuplas (`tuple`), cadenas (`str`) e incluso elementos que no tienen un orden predeterminado como diccionarios (`dict`) o conjuntos (`set`). Otro tipo iterable que ya conocemos es `range`. Incluso, como programadores, podemos definir objetos que sean iterables de esta manera.

```python
for contador in range(5):
    print(contador)
# >> 0  1  2  3  4

for cadena in ['hola', 'adios', 'buenas']:
    print(cadena)
# >> hola  adios  buenas

for cadena in ('tupla', 'de', 'cuatro', 'elementos'):
    print(cadena)
# >> tupla  de  cuatro  elementos

for caracter in 'cadena':
    print(caracter)
# >> c  a  d  e  n  a

for clave in {'software libre': 'bien!', 'software privativo': 'mal :('}:
    print(clave)
# >> software libre  software privativo
```

Podemos transformar cualquier iterable a una lista usando *casting*. Esto normalmente no es necesario y es mucho más eficiente trabajar directamente con el iterable, ya que no necesitamos reservar memoria para la lista, pero hay situaciones donde quizá lo necesitemos.
```python
list(range(15))
# >> [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
```

Sin necesidad de importar ningún módulo, Python ofrece varias utilidades (llamadas *built-ins*) para trabajar con iteradores. La mayoría de estas funciones reciben un iterable y devuelven otro iterable:
```python
def doble(x):
    return x * 2

# "map" aplica una función a cada objeto del iterable
list( map(doble, range(10)) )
# >> [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]

# "filter" se salta los elementos que no cumplan una condición
def es_par(numero):
    return (numero % 2) == 0
list( filter(es_par, range(10)) )
# >> [0, 2, 4, 6, 8]

# "sum" calcula la suma de los elementos de un iterable
sum(range(10))
# >> 45
# Podemos combinar ambos:
sum(map(doble, range(10)))
# >> 90

# "max" y "min": Máximo y mínimo elemento
min(range(10, 20))
# >> 10
max(range(10, 20))
# >> 19

# "zip" une dos iterables distintos
nombres = ['alice', 'bob', 'carol']
pseudonimos = ['A', 'B', 'C']
list(zip(nombres, pseudonimos))
# >> [('alice', 'A'), ('bob', 'B'), ('carol', 'C')]
for nombre, pseudonimo in zip(nombres, pseudonimos):
    print(f'{nombre}: {pseudonimo}')
# >> alice: A
# >> bob: B
# >> carol: C

# "enumerate" adjunta un índice a cada elemento
for i, nombre in enumerate(nombres):
    print(f'{i}: {nombre}')
# >> 0: alice
# >> 1: bob
# >> 2: carol
```

En el módulo `itertools` ([Documentación](https://docs.python.org/3/library/itertools.html)) tenemos muchas más operaciones sobre iterables. Combinando todas estas, podemos hacer casi de todo:
```python
import itertools

# Iteradores infinitos
# (para detener, pulsar Ctrl+C)
for i in itertools.count(start=1, step=2): # Como "range" pero sin final
    print(i)
# >> 1  3  5  7  9  11  ...

for i in itertools.cycle(nombres):
    print(i)
# >> alice  bob  carol  alice  bob  carol ...

# Combinatoria
for numero, nombre in itertools.product(range(2), nombres):
    print(f'{numero} {nombre}')
# >> 0 alice
# >> 0 bob
# >> 0 carol
# >> 1 alice
# >> 1 bob
# >> 1 carol

for permutacion in itertools.permutations(nombres):
    print(permutacion)
# >> ('alice', 'bob', 'carol')
# >> ('alice', 'carol', 'bob')
# >> ('bob', 'alice', 'carol')
# >> ('bob', 'carol', 'alice')
# >> ('carol', 'alice', 'bob')
# >> ('carol', 'bob', 'alice')

for pareja in itertools.combinations(nombres, 2):
    print(pareja)
# >> ('alice', 'bob')
# >> ('alice', 'carol')
# >> ('bob', 'carol')
```

!!! info "Nota"
    Si no entiendes cómo funciona alguna de las funciones de `itertools`, en [la documentación](https://docs.python.org/3/library/itertools.html) tienes una pequeña implementación de cada una para que puedas analizarla paso por paso.

!!! tip "Consejo"
    Los iterables y las operaciones sobre ellos son una de las herramientas más potentes de Python, con las que puedes hacer casi de todo de forma muy escueta y elegante.
    
    Aprende a usarlos, practica mucho y verás como tus habilidades programando mejoran muchísimo. Cuando expresas la solución a un problema mediante iterables y estas operaciones ¡quizá aprendas algo nuevo sobre el problema que no sabías antes!
