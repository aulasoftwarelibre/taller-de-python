"""
for item in list:
    if conditional:
        expression

[ expression for item in list if conditional ]

"""

# Inicializamos la `lista`
lista = []

# Añadimos valores a la `lista`
for n in range(0,11):
    if n%2==0: #se ejecuta la condición en este caso que el número sea par
        lista.append(n**2) #elevamos el numero al cuadrado y lo añadimos a la lista

# imprimimos la `lista`
print(lista)

# Inicializamos la `lista`
lista = [n**2 for n in range(0,12) if n%2==0] #Es lo mismo que antes pero en una sola linea

# Imprimimos la `lista`
print(lista)