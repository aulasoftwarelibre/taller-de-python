# Operaciones matemáticas: `math`

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
from fractions import Fraction
Fraction(10,9) / Fraction(7,8)
# >> Fraction(80, 63)
```
