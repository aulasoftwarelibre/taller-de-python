# Operadores Aritméticos

Si queremos que nuestro programa realice operaciones aritméticas debemos de saber cuales son y como funcionan estos operadores

### Python

```python
"""
+ suma
- resta
* multiplicación
** exponente
/ división
// división sin decimales
% módulo
= asignación
a += b equivale a: a = a + b
a -= b equivale a: a = a - b
a *= b equivale a: a = a * b
a /= b equivale a: a = a / b
a //= b equivale a: a = a // b
a %= b equivale a: a = a % b 
En python no tenemos los operadores ++ o --
para iterar tenemos que hacer uso de los
anteriores
a +=1
a -=1
"""

a = 3

#Incremento ++a

a +=1
print(a)

#Decremento  --a

a -= 1
print(a)

#No existe una equivalencia de a++ o a--
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