# Módulos 


Python es un lenguaje que viene con "pilas incluidas": la librería estándar del intérprete incluye de serie multitud de *módulos*.

A continuación se comentan algunos de estos módulos que te ayudarán a realizar operaciones complejas de manera inmediata.

## Módulos básicos


### Operaciones matemáticas: `math`

```python
import math

# Constantes
math.pi
# > 3.141592653589793
math.e
# > 2.718281828459045

# Funciones especiales
math.sqrt(2) # Raíz cuadrada
# > 1.4142135623730951
math.log(5) # Logaritmo natural (base e)
# > 1.6094379124341003

# Funciones trigonométricas
math.sin(math.pi / 2) # Función seno
# > 1.0
math.cosh(2) # Función coseno hiperbólico
# > 3.7621956910836314
math.radians(30) # Pasar de grados a radianes
# > 0.5235987755982988 (~ pi/6)

# Miscelánea
math.gcd(12, 34) # Máximo común divisor
# > 2
math.prod([3, 5, 7]) # Productorio
# > 105 (3 * 5 * 7)
math.factorial(7) # Factorial
# > 5040
```

### Operaciones sobre cadenas: `string`

TODO
### Copiado de objetos: `copy`

TODO

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
