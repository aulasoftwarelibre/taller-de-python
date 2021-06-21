"""
for target_list in expression_list:
  pass

while expression:
  pass
"""

# "main"

print("---------while---------")
contador = 1

while contador <= 100:
  print(f"Estoy en el numero: {contador}")
  contador = contador + 1

print("---------do while---------")
#Hacemos que la condición se cumpla por defecto
#antes de entrar al bucle obligando así a la pimera iteración
condition = False

while not condition:
    estacion = input('Introduce el nombre de una estación del año: ')
    condition = estacion.lower() in ['primavera', 'verano', 'otoño', 'invierno']
    if not condition:
        print(f"\"{estacion}\" no es el nombre de una estación del año.")
        print('Vuelva a intentarlo.')
print("Muy bien.")

print("---------for---------")
numero = int(input("¿De que número quieres ver la tabla?: "))
print(f"----Tabla del {numero}----")
for numero_tabla in range(1,11):
  print(f"{numero} x {numero_tabla} = {numero_tabla*numero}")