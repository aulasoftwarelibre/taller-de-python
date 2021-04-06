# Operadores Aritméticos

Si queremos que nuestro programa realice operaciones aritméticas debemos de saber cuáles son y cómo funcionan estos operadores

### Python

```python
# Suma
3 + 2  # = 5

# Resta
3 - 2  # = -1

# Multiplicación
3 * 2  # = 6

# Exponenciación ("elevado a")
3 ** 2  # = 9

# División con decimales (a veces denominada "true division")
3 / 2  # = 1.5

# División entera (se ignora el resto de la división)
3 // 2  # = 1

# Módulo ("resto de dividir entre...")
3 % 2  # = 1

# Abreviaturas
a += b  # Equivalente a "a = a + b"
a -= b  # Equivalente a "a = a - b"
a *= b  # Equivalente a "a = a * b"
a /= b  # Equivalente a "a = a / b"
a //= b  # Equivalente a "a = a // b"
a %= b  # Equivalente a "a = a % b"

# En python no tenemos los operadores ++ o --
# Para incrementar tenemos que hacer uso de los anteriores
a +=1
a -=1
```

### C++

```cpp
/*
+ suma
- resta
* multiplicación
/ división
% módulo
= asignación
a += b equivale a: a = a + b
a -= b equivale a: a = a - b
a *= b equivale a: a = a * b
a /= b equivale a: a = a / b
a %= b equivale a: a = a % b
Los 4 incrementan y decrementan pero 
a++ equivale a: devolver el dato y luego incrementarlo
a-- equivale a: devolver el dato y luego decrementarlo
++a equivale a: incrementar el dato y luego devolverlo 
--a equivale a: decrementar el dato y luego devolverlo
*/



#include <cstdio>
#include <cstdlib>
#include <iostream>
using namespace std;

int main(int argc, char const *argv[])
{
  int a = 3;
  cout<<a++<<"\n";
  cout<<++a<<"\n";
  cout<<a--<<"\n";
  cout<<--a<<"\n";
  return 0;
}
```

!!! warning "Cuidado"
    En C/C++, la asignación (`#!c =`) se considera un operador, cuyo valor es el valor de la variable de la izquierda del `#!c =` después de realizar la asignación. Por tanto, la siguiente línea es totalmente válida:
    
    ```c
    int a, b;
    a = b = 3;
    // Equivalente a:
    a = (b = 3);
    // Tanto "a" como "b" tienen asignados el valor 3
    ```
    
    Esto puede leerse como:
    
    * La sentencia `#!c a = (b = 3)` consiste en evaluar la expresión `#!c a = (b = 3)`
        * Evaluar la expresión `#!c a = (b = 3)` consiste en evaluar la expresión `#!c b = 3` y asignar su valor a `#!c a`, el valor de la expresión es el nuevo valor de `#!c a`.
            * Evaluar la expresión `#!c b = 3` consiste en evaluar la expresión `#!c 3` y asignar su valor a `#!c b`, el valor de la expresión es el nuevo valor de `#!c b`.
    
    Aunque puede ser útil y elegante en ocasiones, en otras puede ser una mala práctica. El problema más común que nos podemos encontrar es una errata del siguiente tipo:
    ```c
    int a;
    // ...
    if (a = 3) { // Errata: realmente queríamos comparar si "a == 3"
                 // En su lugar, se asignará el valor 3 a "a" y se
                 // ejecutará el bloque ya que 3 != 0
        // ...
    }
    ```
    
    En Python, la asignación *NO es un operador*, sino una sentencia
    ```python
    a = 3  # Válido
    if a = 3:  # Error de sintáxis, el programa falla
        ...
    ```
    
    Recientemente se añadió al estándar el *operador morsa* (`#!python :=`) que funciona como la asignación de C, pero generalmente sólo es útil en situaciones muy concretas, puedes ignorarlo por ahora.
