# Cadenas

Si empezamos trabajar con la entrada y salida por consola resulta imprescindible conocer el funcionamiento de las cadenas ya que la entrada que recibamos a través de estas operaciones de E/S tendrá este formato.

### Python

```python
mi_texto = '"Taller"' #Al usar comillas de diferente tipo no interfieren
mi_texto2 = "de \"Python\"" # El \ hace que se ignore el caracter siguiente para que no cierre comillas

texto_unido = mi_texto + " " + mi_texto2
print(texto_unido)

texto_unido = mi_texto + "\n " + mi_texto2 #Salta de linea
print(texto_unido)

texto_unido = mi_texto + "\t " + mi_texto2 #Tabula
print(texto_unido)

texto_unido = mi_texto + "\r " + mi_texto2 #Borra lo anterior
print(texto_unido)
```

### C++

```cpp
#include <cstdio>
#include <cstdlib>
#include <iostream>
using namespace std;

int main()
{
  string mi_texto = "\"Taller\"";// El \ hace que se ignore el caracter siguiente para que no cierre comillas 
  string mi_texto2 = "de \"Python\""; 
  string texto_unido = mi_texto + " " + mi_texto2;
  cout<<texto_unido<<"\n";

  texto_unido = mi_texto + "\n " + mi_texto2; //Salta de linea
  cout<<texto_unido<<"\n";

  texto_unido = mi_texto + "\t " + mi_texto2; //Tabula
  cout<<texto_unido<<"\n";

  texto_unido = mi_texto + "\r " + mi_texto2; //Borra lo anterior
  cout<<texto_unido<<"\n";
  return 0;
}
```