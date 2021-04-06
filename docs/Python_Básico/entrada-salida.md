# Entrada y Salida

Cuando realicemos nuestros primeros programas necesitaremos hacer uso de la entrada y salida para poder interactuar con el usuario y que éste pueda introducir información en nuestros programas. Para ello haremos uso de la entrada y salida por consola.

### Python

```python
#Entrada
cadena = input("Introduce una cadena: ")

#Salida 
print(cadena)

#Como formatear texto y variables en un print
nombre = "Marcos"
apellidos = "Rivera Gavilán"
correo = "riveragavilanmarcos@gmail.com"

print("Hola me llamo " + nombre + " " + apellidos + " y mi correo es " + correo)#El + concatena sin espacios
print(f"Hola me llamo {nombre} {apellidos} y mi correo es {correo}")# Al estar dentro de una cadena ponemos los espacios normalmente
print("Hola me llamo {} {} y mi correo es {}".format(nombre, apellidos, correo))# Al estar dentro de una cadena ponemos los espacios normalmente
```

### C++

```cpp
#include <cstdio>
#include <cstdlib>
#include <iostream>
using namespace std;

int main()
{
  string cadena;
  cout<<"Introduce una cadena: \n";

  //Entrada:
  cin>>cadena;
  
  //Salida
  cout<<cadena<<"\n";
  
  //Como formatear texto y variables en un print
  string nombre = "Marcos";
  string apellidos = "Rivera Gavilán";
  string correo = "riveragavilanmarcos@gmail.com";
  
  cout<<"Hola me llamo "<<nombre<<" "<<apellidos<<" y mi correo es "<<correo<<"\n";//El << concatena sin espacios
  return 0;
}
```
