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
