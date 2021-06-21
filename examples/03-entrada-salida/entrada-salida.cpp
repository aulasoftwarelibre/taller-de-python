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
