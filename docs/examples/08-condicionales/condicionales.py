"""
if expression:
  code

elif expression:
  code

else:
  code

expression1 if condition else expression2
"""









"""
¿Se puede implementar la sentencia switch en Python?

Si y no. Como tal no existe una sentencia switch pero 
si hacemos uso de los diccionarios podemos 
hacer una implementación la cual veremos en el siguiente ejemplo:
"""


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