# Carga de módulos


Cuando trabajamos desde el intérprete, una vez lo cerramos perdemos todo el trabajo que hemos creado. Por tanto, si queremos que nuestro programa perdure, escribiremos el código en un fichero de texto, esto es, un *script*. Python es un lenguaje *interpretado*, luego no es necesario un proceso de compilación como en otros lenguajes como C sino que podemos ejecutar un script directamente.

Por ejemplo, si guardamos nuestro programa un fichero `programa.py`, podemos lanzarlo con el comando:

```bash
python programa.py
```

Sin embargo, en cuanto nuestro programa crezca un poco, necesitaremos partirlo en distintos ficheros para una mejor organización.

Python nos ofrece un mecanismo para guardar definiciones en un fichero para usarlos en un script o directamente en el intérprete: los *módulos*.

Por ejemplo, podemos definir el siguiente fichero `modulo.py`:
```python
# modulo.py

def mutiplicar(a, b):
    return a * b

def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b
```

Así, en nuestro `programa.py` podemos *importar* el módulo con la sintaxis `#!python import <modulo>`. Al igual que como pasa en otros lenguajes (por ejemplo, cuando usamos el `#!c #include "modulo.h"` de C), el intérprete de Python busca primero en el directorio actual y después en las librerías instaladas:
```python
# programa.py

# Por defecto, busca un fichero "modulo.py" en el
# mismo directorio en el que estamos
import modulo

producto = modulo.multiplicar(2, 3)
print(producto)
# >>> 6

suma = modulo.sumar(2, 3)
print(suma)
# >>> 5
```

Podemos asignar un alias al módulo que acabamos de importar con `#!python import <modulo> as <alias>`:
```python
import modulo as mod

producto = mod.multiplicar(2, 3)
print(producto)
# >>> 6

suma = mod.sumar(2, 3)
print(suma)
# >>> 5
```

También podemos importar sólo algunos elementos particulares con `#!python from <modulo> import <elemento>`:
```python
from modulo import sumar
from modulo import restar as rest # También podemos usar alias!

resta = rest(2, 3)
print(resta)
# >>> -1

suma = sumar(2, 3)
print(suma)
# >>> 5
```

!!! warning "Cuidado"
    Existe otra sintaxis con la que podemos importar todos los elementos de un módulo al contexto global:
    
    ```python
    from modulo import *
    suma = sumar(2, 3)
    resta = restar(2, 3)
    producto = multiplicar(2, 3)
    ```
    
    Esto puede parecer cómodo, pero potencialmente *puede causarnos problemas*, ya que podríamos "contaminar" el espacio global con nombres inesperados que sobreescriben algún otro que estemos usando.
    
    **Evita usar esta sintaxis**.

En las secciones a continuación vamos a trabajar con módulos de la librería estándar, así que no es necesario que instalemos nada.
