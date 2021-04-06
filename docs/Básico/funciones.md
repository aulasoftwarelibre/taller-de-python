# Funciones

Si queremos que hacer que nuestro codigo sea lo más mantenible posible a lo largo del tiempo pudiendo  añadir nuevas funcionalidades si que ello suponga un exceso de carga de trabajo debemos de considerar hacer uso de las funciones. Las funciones nos permiten simplificar nuestro programa eliminando bloques de código que se pueden llegar a repetir. Por ejemplo buscar la posición de un elemento en un vector o decir si un número es primo. Si utilizamos funciones podremos separar estas funcionalidades en pequeños bloques de codigo independientes a los que únicamente llamaremos cuando realmente sean necesario pasándole (o no) una serie de valores de entrada para que nos devuelvan una determinada salida.  

### Python

```python
def a(b):
  return 1+b

def b(i, f):
  return 1.3+f

def c():
  return True

def d():
  print("hola")
```

### C++

```cpp
#include <cstdio>
#include <cstdlib>
#include <iostream>
using namespace std;

int a(int b)
{
  return 1+b;
}

float b(int b, float a)
{
  return 1.3+a;
}

bool c()
{
  return true;
}

void d()
{
  cout<<"hola"<<"\n";
}
```

Tal y como podemos obeservar, a diferencia de C++ las funciones de Python no equieren especificar el tipo de dato que devolverá como salida ya que como previamente hemos dicho al ser de tipado dinámico el lenguaje se encarga de todo.