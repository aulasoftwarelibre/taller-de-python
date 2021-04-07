# Argumentos

En Python existen distintos tipos de argumentos que debemos de conocer ya que entenderlos nos ayudará muchísimo a la hora de programar y de consultar la documentación. En concreto debemos de distinguir entre:

- Los argumentos posicionales: son argumentos que se pueden llamar por su posición en la definición de la función.

- Los argumentos de palabras: clave son argumentos que se pueden llamar por su nombre.

- Los argumentos obligatorios: son argumentos que se deben pasar a la función.

- Los argumentos opcionales: son argumentos que no se pueden pasar a la función. En python, los argumentos opcionales son argumentos que tienen un valor predeterminado.

La forma en que se pasa el valor a la función determina si son argumentos posicionales o argumentos de palabra clave .
Por ejemplo, las tres siguientes llamadas a la función rectangleArea() serían válidas y devolverían el mismo resultado.

```Python
def rectangleArea(width, height):
    return width * height

rectangleArea(1, 2) # positional arguments

rectangleArea(height=2, width=1)# keyword arguments

rectangleArea(width=1, height=2)# keyword arguments

```

Una vez hemos entendido ese concepto y las diferencias de significados entre los distintos tipos podemos combinarlos como queramos aquí teneis algunos ejemplos:

## Argumento posicional que es opcional

```Python

def f(a=2, /):
    pass


f()  # Allowed, argument is optional
f(1)  # Allowed, it's a positional argument
f(a=1)  # Error, positional only argument

```

## Argumento posicional que se requiere

```Python

def f(a, /):
    pass


f()  # Error, argument required
f(1)  # Allowed, it's a positional argument
f(a=1)  # Error, positional only argument

```

## Argumento de palabra clave que es opcional

```Python

def f(*, a=1):
    pass


f()  # Allowed
f(1)  # Error, keyword only arguments
f(a=1)  # Allowed, it's a keyword argument

```

## Argumento de palabra clave que se requiere

```Python

def f(*, a)
    pass


f()  # Error, argument required
f(1)  # Error, keyword only arguments
f(a=1)  # Allowed, it's a keyword argument

```

## Argumento posicional y de palabra clave que es opcional

```Python

def f(a=1)
    pass


f()  # Allowed, argument is optional
f(1)  # Allowed, it's a positional argument
f(a=1)  # Allowed, it's a keyword argument

# De hecho esta funcion equivale a:
def f(*, a=1, /):
    pass

```

## Argumento posicional y de palabra clave que se requiere

```Python

def f(a):
    pass


f()  # Error, argument required
f(1)  # Allowed, it's a positional argument
f(a=1)  # Allowed, it's a keyword argument

# De hecho esta funcion equivale a:
def f(*, a, /):
    pass

```