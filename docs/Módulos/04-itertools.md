# Iteradores: `itertools`

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
