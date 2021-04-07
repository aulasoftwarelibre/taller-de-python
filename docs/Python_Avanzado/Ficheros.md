# Ficheros

Si queremos hacer que nuestros programas sean capaces de almacenar información y que la puedan recuperar posteriormente aunque hayamos reiniciado nuestro ordenador podemos hacer uso de los ficheros

En python los ficheros se abren con la función open(). Como primer parámetro se pasa el nombre del fichero y como segundo parámetro una cadena con caracteres similares a los de fopen() de C. Estos son varios ejemplos de la sintaxis:

## Abrir ficheros

- Abrir fichero para lectura :              f = open("fichero.txt", "r")
- Abrir fichero para lectura en binario :   f = open("fichero.txt", "rb")
- Abrir fichero para escribir desde cero :  f = open ("fichero.txt", "w")
- Abrir fichero para añadir al final :      f = open ("fichero.txt", "a")
- Abrir fichero para lectura y escritura :  f = open("fichero.txt", "r+")


## Leer de ficheros

Para leer del fichero, podemos usar las funciones f.read() y f.readline()

- Lectura de todo el fichero de golpe : fichero = f.read()
- Lectura de 100 caracteres : dato = f.read(100)
- Lectura de una línea completa : linea = f.readline()

## Escribir en ficheros

Para escribir el fichero haremos uso de f.write() y la forma de escribir dependerá de como hayamos abierto el archivo:

- Para escribir el fichero desde cero, machacando su contenido si lo hubiera: f=open("fichero.txt","w")

- Para escribir el fichero desde cero, machacando su contenido si lo hubiera: f=open("fichero.txt","a")

## Moverse por el fichero

Con f.tell() podemos saber en qué posición estamos del fichero y con f.seek() podemos desplazarnos por él, para leer o escribir en una determinada posición.

- f.seek(n) : Ir al byte n del fichero
- f.seek(n,0) : Equivalente al anterior
- f.seek(n,1) : Desplazarnos n bytes a partir de la posición actual del fichero
- f.seek(n,2) : Situarnos n bytes antes del final de fichero.

El segundo parámetro en estos ejemplos es

- Ninguno o 0 : la posición es relativa al principio del fichero
- 1 : la posición es relativa a la posición actual
- 2 : la posición es relativa al final del fichero y hacia atrás.

## Bucle para leer un fichero

A modo de ejemplo, el siguiente programa python abre un fichero y lo copia en otro

```Python
f = open("origen.txt")
g = open("destino.txt","w")
for linea in f:
   g.write(linea)
g.close()
f.close()
```

Lo interesante aquí es el bucle "for linea in f". Esta es una forma de recorrer un fichero de texto, obteniendo una línea cada vez.

El fichero se puede leer con f.readLine() que nos da una línea cada vez, incluyendo el salto de linea \n al final. Cuando lleguemos a final de fichero nos devolverá una linea vacía. Una línea en blanco en medio del fichero nos sería devuelta como un "\n", no como una línea vacía "". El siguiente ejemplo hace la copia del fichero leyendo con readline() y en un bucle hasta fin de fichero.

```Python
f = open("origen.txt")
g = open("destino.txt","w")
linea = f.readline()
while linea != "":
   g.write(linea)
   linea = f.readline()
g.close()
f.close()
```

## Cerrar ficheros

Para cerrarlo, basta llamar a f.close()