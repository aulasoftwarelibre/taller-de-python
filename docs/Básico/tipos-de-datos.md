# Tipos de Datos

Cuando programamos, necesitamos poder almacenar información para poder utilizarla posteriormente. Para ello hacemos uso de las variables. El contenido que una variable puede almacenar dependerá del tipo de dato con el que se identifica. Así una variable de tipo bool podrá almacenar True o False pero no un 5 ya que este se corresponde con un tipo de dato int. Python es un lenguaje débilmente tipado por lo que no es necesario especificar el tipo de dato que almacenará la variable cuando la creamos ya que Python se encarga de hacerlo por nosotros. Aun así Python como todos los lenguajes posee sus propios tipos de datos que son los siguientes:

### Python

```python
a = 1 #int
print(type(a))

b = "Hello World" #str
print(type(b))

c = True #bool
print(type(c))

d = 3,14 #float
print(type(d))

e = 1j #complex
print(type(e))

f = [1, 3.3, "python"] #list es una lista de datos
print(type(f))

g = (1, 3.3, "python") #tuple es una lista constante
print(type(g))

h = {1, 3.3, "python"} #set colección de datos desordenada
print(type(h))

i = {1:"python", "key":3.3, 4.4:"a"} #dict colección de pares calve-valor
print(type(i))

#Ejemplo de uso de una lista

diccionario = {1:a, 2:b, 3:c, 4:d, 5:e, 6:f, 7:g, 8:h, 9:i}
print("------------------------")
for j in range (1,10):
  print(type(diccionario[j]))
```

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