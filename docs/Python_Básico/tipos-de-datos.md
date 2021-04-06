# Tipos de datos

Cuando programamos, necesitamos poder almacenar información para poder utilizarla posteriormente. Para ello hacemos uso de las *variables*.

En lenguajes de tipado estático, como C o C++, el contenido que una variable puede almacenar estará limitado por su tipo asociado. Así una variable de tipo `#!c++ bool` podrá almacenar `#!c++ true` o `#!c++ false` pero no `#!c++ 5` ya que éste se corresponde con un tipo de dato `#!c++ int`.

Python en cambio es un lenguaje de *tipado dinámico*, por lo que no es necesario especificar el tipo de dato que almacenará la variable cuando la creamos ya que Python se encarga de hacerlo por nosotros. Aun así, Python, como todos los lenguajes posee sus propios tipos de datos que son los siguientes:

### Python

```python
numero_entero = 1 #int
print(type(numero_entero))

cadena = "Hello World" #str
print(type(cadena))

booleano = True #bool
print(type(booleano))

coma_flotante = 3.14 #float
print(type(coma_flotante))

numero_complejo = 1j #complex
print(type(numero_complejo))

lista = [1, 3.3, "python"] #list es una lista de datos
print(type(lista))

tupla = (1, 3.3, "python") #tuple es una lista constante
print(type(tupla))

conjunto = {1, 3.3, "python"} #set colección de datos únicos desordenada
print(type(conjunto))

diccionario = {1:"python", "key":3.3, 4.4:"a"} #dict colección de pares clave-valor, también denominado "tabla hash"
print(type(diccionario))

# Cómo recorrer una colección

l = [numero_entero, cadena, booleano, coma_flotante,
     numero_complejo, lista, tupla, conjunto, diccionario]
print("------------------------")
# Podemos usar un índice "j"
for j in range(len(l)):
  elemento = l[j]
  print(type(elemento))
  
# Podemos o recorrer directamente la lista
for elemento in l:
  print(type(elemento))
```

!!! warning "Cuidado"
    En Python el siguiente código es válido:
    ```python
    a = 3
    print(a)
    a = 'cadena'
    print(a)
    ```
    
    Si bien es válido, es recomendable *evitar* en la medida de lo posible que una misma variable (en este caso `a`) haga referencia a valores de distinto tipo durante su tiempo de vida. Simplemente, ¡usa una nueva variable!
    

### C++

```cpp
#include <cstdio>
#include <cstdlib>
#include <iostream>
using namespace std;

//Comentar como se definen las variables

int main()
{
  int a = 0;
  char b;
  bool c;
  float d;
  double e; //almacenan más digitos que los floats
  wchar_t g; //su tamaño es superior a los habituales 8 bits
  return 0;
}
```
