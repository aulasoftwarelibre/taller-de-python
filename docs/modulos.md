# Módulos 


Python es un lenguaje que viene con "pilas incluidas": la librería estándar del intérprete incluye de serie multitud de *módulos*.

A continuación se comentan algunos de estos módulos que te ayudarán a realizar operaciones complejas de manera inmediata.

## Módulos básicos


### Operaciones matemáticas: `math`

[Documentación](https://docs.python.org/3/library/math.html)

```python
import math

# Constantes
math.pi
# >> 3.141592653589793
math.e
# >> 2.718281828459045

# Funciones especiales
math.sqrt(2) # Raíz cuadrada
# >> 1.4142135623730951
math.log(5) # Logaritmo natural (base e)
# >> 1.6094379124341003

# Funciones trigonométricas
math.sin(math.pi / 2) # Función seno
# >> 1.0
math.cosh(2) # Función coseno hiperbólico
# >> 3.7621956910836314
math.radians(30) # Pasar de grados a radianes
# >> 0.5235987755982988 (~ pi/6)

# Miscelánea
math.gcd(12, 34) # Máximo común divisor
# >> 2
math.prod([3, 5, 7]) # Productorio
# >> 105 (3 * 5 * 7)
math.factorial(7) # Factorial
# >> 5040
```

### Operaciones sobre cadenas: `str`

```python
'escribir En Mayúsuclas y miNúsculas'.capitalize()
# >> 'Escribir en mayúsuclas y minúsculas'

'uno, dos, tres'.split(', ')
# >> ['uno', 'dos', 'tres']

'''Esto es una cadena multilínea.
Puedes escribir saltos de línea entre medias.
Esto es un ejemplo y no se me ocurre qué más poner'''.splitlines()
# >> ['Esto es una cadena multilínea.', 'Puedes escribir saltos de línea entre medias.', 'Esto es un ejemplo y no se me ocurre qué más poner']

entero = 3
flotante = 2.1
cadena = 'hola'

'Igual que printf en C, puedes imprimir valores: %d' % entero
# >> 'Igual que printf en C, puedes imprimir valores: 3'

'Puedes poner más de un valor: %d y "%s"' % (entero, cadena)
# >> 'Puedes poner más de un valor: 3 y "hola"'

'Y puedes especificar el formato: %.3f' % flotante
# >> 'Y puedes especificar el formato: 2.100'

'Otra forma de formatear es con el método "format": {}'.format(entero)
# >> 'Otra forma de formatear es con el método "format": 3'

'Puedes especificar el orden: {2}, {0}, {1}'.format(entero, flotante, cadena)
# >> 'Puedes especificar el orden: hola, 3, 2.1'

'O incluso llamarlos por su nombre: {n}, {f}, {c}'.format(n=entero, f=flotante, c=cadena)
# >> 'O incluso llamarlos por su nombre: 3, 2.1, hola'

f'A partir de Python 3.6 puedes usar "f-strings": {entero}, {flotante:.3f}, {cadena}'
# >> 'A partir de Python 3.6 puedes usar "f-strings": 3, 2.100, hola'
```

### Copiado de objetos: `copy`

[Documentación](https://docs.python.org/3/library/copy.html)

```python
a = ['hola', 'adios', 'buenas']
b = a  # Copiamos la referencia, NO SE HACE COPIA
b[0] = 'hastaluego'  # Estamos modificando la lista original
print(a)
# >> ['hastaluego', 'adios', 'buenas']
print(b)
# >> ['hastaluego', 'adios', 'buenas']


import copy

a = ['hola', 'adios', 'buenas']
b = copy.copy(a)  # Creamos una copia de la lista
b[0] = 'hastaluego'  # Estamos modificando la copia
print(a)
# >> ['hola', 'adios', 'buenas']
print(b)
# >> ['hastaluego', 'adios', 'buenas']

a = [[1, 2], [3, 4], [5, 6]]
b = copy.copy(a)  # Copiamos las referencias, pero apunta a las mismas listas
b[0][1] = 10  # Ojo, estamos cambiando la primera lista
print(a)
# >> [[1, 10], [3, 4], [5, 6]]

# Necesitamos una copia "profunda"
a = [[1, 2], [3, 4], [5, 6]]
b = copy.deepcopy(a)  # Ahora sí, creamos una copia de las listas anidadas
b[0][1] = 10
print(a)
# >> [[1, 2], [3, 4], [5, 6]]
print(b)
# >> [[1, 10], [3, 4], [5, 6]]
```

### Generadores aleatorios: `random`

TODO

### Fechas y horas: `datetime`

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
