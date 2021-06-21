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

