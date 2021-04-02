# Operaciones sobre cadenas: `str`

Uno de los puntos fuertes de Python es la facilidad del manejo de cadenas. Tenemos mucha flexibilidad para definir cadenas y además disponemos de muchas operaciones sobre ellas:
```python
'escribir En Mayúsuclas y miNúsculas'.capitalize()
# >> 'Escribir en mayúsuclas y minúsculas'

'uno, dos, tres'.split(', ')
# >> ['uno', 'dos', 'tres']

'''Esto es una cadena multilínea.
Puedes escribir saltos de línea entre medias.
Esto es un ejemplo y no se me ocurre qué más poner'''.splitlines()
# >> ['Esto es una cadena multilínea.', 'Puedes escribir saltos de línea entre medias.', 'Esto es un ejemplo y no se me ocurre qué más poner']
```

Si tenemos que construir cadenas a partir de variables en nuestro código tenemos varias formas de hacerlo.

El método original se parece mucho a cómo lo hacemos en C con la función `printf`. Para ello, usamos el operador `%` sobre una cadena.
```python
entero = 3
flotante = 2.1
cadena = 'hola'

'Igual que printf en C, puedes imprimir valores: %d' % entero
# >> 'Igual que printf en C, puedes imprimir valores: 3'

'Puedes poner más de un valor: %d y "%s"' % (entero + 2, cadena)
# >> 'Puedes poner más de un valor: 5 y "hola"'

'Y puedes especificar el formato: %.3f' % flotante
# >> 'Y puedes especificar el formato: 2.100'
```

También podemos usar el método `.format()`, que nos permite mayor flexibilidad en el orden de los parámetros y puede hacer el código más legible.
```python
'Otra forma de formatear es con el método "format": {}'.format(entero)
# >> 'Otra forma de formatear es con el método "format": 3'

'Puedes especificar el orden: {2}, {0}, {1}'.format(entero, flotante, cadena)
# >> 'Puedes especificar el orden: hola, 3, 2.1'

'O incluso llamarlos por su nombre: {n}, {f}, {c}'.format(n=entero+1, f=flotante*2, c=cadena)
# >> 'O incluso llamarlos por su nombre: 4, 4.2, hola'
```

Por último, desde la versión 3.6, podemos integrar las propias expresiones dentro de la cadena usando lo que se denomina "f-strings":
```python
f'A partir de Python 3.6 puedes usar "f-strings": {entero + 1}, {flotante * 2:.3f}, {cadena}'
# >> 'A partir de Python 3.6 puedes usar "f-strings": 4, 4.200, hola'
```

!!! tip "Consejo"
    Ahí fuera encontrarás programas que utilizan cualquier combinación de los tres métodos anteriores (siempre el mismo o mezclados). Nuestro consejo es que, siguiendo los principio de "código limpio", *trates de adherirte a un sólo método dentro del mismo repositorio de código* para facilitar la lectura.
    
    Si se trata de código desde cero y se usa una versión compatible, *recomendamos usar los f-string* por ser generalmente más legibles y cómodos.
    
    Eso sí, en situaciones concretas podría tener más sentido usar uno sobre los demás. ¡Piensa bien lo que haces y ponte en el lugar de alguien leyendo tu código!
