# Módulos 


Python es un lenguaje que viene con "pilas incluidas": la librería estándar del intérprete incluye de serie multitud de *módulos*.

A continuación se comentan algunos de estos módulos que te ayudarán a realizar operaciones complejas de manera inmediata.

## Módulos básicos


### Operaciones matemáticas: `math`

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

### Operaciones sobre cadenas: `str`

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

### Copiado de objetos: `copy`

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

### Generadores aleatorios: `random`

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

### Tiempo, fechas y horas: `time`, `datetime`, `calendar`

TODO

### Programación funcional: `itertools` y `functools`

## Módulos avanzados

### Expresiones regulares: `re`

TODO

### Manejo de rutas del sistema de archivos: `pathlib`

TODO

### Logging: `logging`

TODO

### Manejo de ficheros JSON: `json`

TODO

### Serialización: `pickle`

TODO
