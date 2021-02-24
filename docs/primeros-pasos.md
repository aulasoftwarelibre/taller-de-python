# Primeros Pasos

Una vez hemos hecho nuestro primer programa llega la hora de profundizar un poco más en este lenguaje. Para ayudar a relacionar conceptos y entenderlo todo un poco mejor todos los ejemplos de código del curso estarán acompañados de una implementación similar en C++ que puede ser compliada y ejecutada para comprobar los resultados y ver las similitudes y diferencias entre ambos lenguajes.

## Comentarios

Una de las cosas más importantes a la hora de programar son los comentarios. En Python como en otros muchos lenguajes existen distintos tipos de comentarios que usaremos en base al contexto y a nuestras necesidades. 

### Python: <a href="/examples/02-comentarios/comentarios.py" download>comentarios.py</a>

```python
# Esto mostrará el texto hola por la consola

print("Hola")

# Estas dos instrucciones muestran codigo por pantalla

print("mundo")

# print("!!")

"""
Esto no se mostrará:
print("Esto no se va a mostrar")
print("Porque estará en dentro de un comentario multilinea")
"""

print("Adios!!")
```

### C++ <a href="/examples/02-comentarios/comentarios.cpp" download>comentarios.cpp</a>

```cpp
#include <cstdio>
#include <cstdlib>
#include <iostream>
using namespace std;

int main()
{
  //Esto mostrará el texto hola por la consola
  cout<<"Hola\n";

  //Estas dos instrucciones muestran código por pantalla

  cout<<"mundo\n";

  //cout<<"!!\n";

  /* 
  Esto no se mostrará:
  cout<<"Esto no se va a mostrar"
  cout<<"Porque estará dentro de un comentario multilinea"
  */

  cout<<"Adios!!\n";
  return 0;
}
```

## Tipos de Datos 