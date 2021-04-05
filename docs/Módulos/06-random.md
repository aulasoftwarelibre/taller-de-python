# Generadores aleatorios: `random`

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
