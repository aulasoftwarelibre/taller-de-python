# Cadenas

Empezaremos trabajando con la entrada y salida por consola. Resulta imprescindible conocer el funcionamiento de las cadenas ya que la entrada que recibamos a través de estas operaciones de E/S tendrá este formato.

### Python

```python
# Podemos usar comillas dobles ("") o simples ('')
# para definir cadenas
mi_texto = '"Taller"' # Podemos usar las comillas de distinto tipo dentro
                      # de la cadena sin que interfieran
mi_texto2 = "de \"Python\"" # El \ actúa como "carácter de escape"
                            # Hace que se ignore el carácter siguiente
                            # para que no cierre comillas

texto_unido = mi_texto + " " + mi_texto2
print(texto_unido)

texto_unido = mi_texto + "\n " + mi_texto2 #Salto de línea
print(texto_unido)

texto_unido = mi_texto + "\t " + mi_texto2 # Tabulación
print(texto_unido)

texto_unido = mi_texto + "\r " + mi_texto2 # Borra lo anterior
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
  string mi_texto = "\"Taller\"";// El \ actúa como "carácter de escape" y
                                 // hace que se ignore el caracter siguiente
                                 // para que no cierre comillas 
  string mi_texto2 = "de \"Python\""; 
  string texto_unido = mi_texto + " " + mi_texto2;
  cout<<texto_unido<<"\n";

  texto_unido = mi_texto + "\n " + mi_texto2; // Salto de línea
  cout<<texto_unido<<"\n";

  texto_unido = mi_texto + "\t " + mi_texto2; // Tabulación
  cout<<texto_unido<<"\n";

  texto_unido = mi_texto + "\r " + mi_texto2; // Borra lo anterior
  cout<<texto_unido<<"\n";
  return 0;
}
```
