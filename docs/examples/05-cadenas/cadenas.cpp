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
