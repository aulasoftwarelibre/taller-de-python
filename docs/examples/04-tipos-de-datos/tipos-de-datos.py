#Comentar como se definen las bariables

a = 1 #int
print(type(a))

b = "Hello World" #str
print(type(b))

c = True #bool
print(type(c))

d = 3,14 #float
print(type(d))

e = 1j #complex
print(type(e))

f = [1, 3.3, "python"] #list es una lista de datos
print(type(f))

g = (1, 3.3, "python") #tuple es una lista constante
print(type(g))

h = {1, 3.3, "python"} #set colección de datos desordenada
print(type(h))

i = {1:"python", "key":3.3, 4.4:"a"} #dict colección de pares calve-valor
print(type(i))

#Ejemplo de uso de una lista

diccionario = {1:a, 2:b, 3:c, 4:d, 5:e, 6:f, 7:g, 8:h, 9:i}
print("------------------------")
for j in range (1,10):
  print(type(diccionario[j]))