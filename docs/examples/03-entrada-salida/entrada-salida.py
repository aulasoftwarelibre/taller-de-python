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