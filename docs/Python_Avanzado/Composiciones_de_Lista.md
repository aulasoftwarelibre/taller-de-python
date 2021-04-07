# Composiciones de Lista

Esta es otra funcionalidad interesante de Python. Supongamos que queremos separar las letras de la palabra human y añadirlas como elementos de una lista. Lo primero que se nos viene a la mente es usar un bucle for.

## Ejemplo 1: iterando a través de una cadena usando un for 

```Python
h_letters = []

for letter in 'human':
    h_letters.append(letter)

print(h_letters)
```

Cuando ejecutamos el programa, la salida será:

['h', 'u', 'm', 'a', 'n']

Sin embargo, Python tiene una forma más sencilla de resolver este problema mediante la composición de listas. La composición de listas es una forma elegante de definir y crear listas basadas en listas existentes.

## Sintaxis de la comprensión de listas

```Python
[expresion for item in list]
```

Veamos cómo se puede escribir el programa anterior usando las composiciones de lista.

## Ejemplo 2: iterar a través de una cadena usando las composiciones de lista

```Python
h_letters = [ letter for letter in 'human' ]
print( h_letters)
```
Cuando ejecutamos el programa, la salida será:

['h', 'u', 'm', 'a', 'n']

En el ejemplo anterior, se asigna una nueva lista a la variable h_letters, y la lista contiene los elementos de la cadena iterable 'human'. Llamamos a la función print() para imprimir la salida.

## Extra

Podemos complicarlo todo lo que queramos y por ejemplo añadir condicionales. Analiza el siguiente ejemplo:

```Python
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
```