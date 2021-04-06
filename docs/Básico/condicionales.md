# Condicionales

Conforme vayamos avanzando nuestros programas serán cada vez más complicados y es posible que necesitemos hacer uso de estructuras condicionales que nos permitan direccionar ejecutar determinadas secciones de nuestro codigo si se cumplen determinadas condiciones. Para ello haremos uso de las estructuras condicionales que en Python son las siguientes:

### Python

```python

if expression:
  code

elif expression:
  code

else:
  code

expression1 if condition else expression2 #Operador ternario

```

### C++

```cpp
  if ( condition )
  {
     code 
  }

  else
  {
     code 
  }

  else if ( condition )
  {
     code 
  }
  
  condition ? expression1 : expression1; //Operador ternario

  switch (expression)
  {
  case  constant-expression :
     code 
    break;
  
  default:
    break;
  }
```

Podemos observar que en ambos lenguajes tenemos las mismas estructuras aunque en C++ además podemos hacer uso de la estructura Switch que en Python no está incluida. Pese a que se considera un antipatrón para todos aquellos que esteis acostumbrados a usarla esta podría ser una posible implementación en Python haciendo uso de los diccionarios:

### Python

```python

# "main"
mes = int(input("Introduce un numero para obtener el mes que le corresponde:"))
switch = {
1: "Enero",
2: "Febrero",
3: "Marzo",
4: "Abril",
5: "Mayo",
6: "Junio",
7: "Julio",
8: "Agosto",
9: "Septiembre",
10: "Octubre",
11: "Noviembre",
12: "Diciembre"
}
print(switch.get(mes, "No existe un mes equivalente al numero introducido"))

```

Y ésta sería una posible implementación en el caso de que quisiésemos utilizar funciones (se verán posteriormente):

```python

def uno():
    print("Enero")
 
def dos():
    print("Febrero")
 
def tres():
    print("Marzo")
 
def cuatro():
    print("Abril")
 
def cinco():
    print("Mayo")
 
def seis():
    print("Junio")
 
def siete():
    print("Julio")
 
def ocho():
    print("Agosto")
 
def nueve():
    print("Septiembre")
 
def diez():
    print("Octubre")
 
def once():
    print("Noviembre")
 
def doce():
    print("Diciembre")
 
 
# "main"
mes=int(input("Introduce un numero para obtener el mes que le corresponde: "))
switch = {
    1: uno,
    2: dos,
    3: tres,
    4: cuatro,
    5: cinco,
    6: seis,
    7: siete,
    8: ocho,
    9: nueve,
    10: diez,
    11: once,
    12: doce
}
# Obtiene la función del diccionario. 
# Si argument no se corresponde con ningún indice 
# func obtendrá la función lambda equivaliendo esto al default
func = switch.get(mes, lambda: print("No existe un mes equivalente al numero introducido"))
# Para ejecutar la función obtenida usamos:
func()
```
