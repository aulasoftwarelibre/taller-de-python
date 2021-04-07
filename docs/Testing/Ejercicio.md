# Ejercicio

## Enunciado
Supongamos que tenemos que implementar una función que calcule el factorial de un numero. Si seguimos al pie de la letra las indicaciones de TDD lo primero que tenemos que hacer es crear la función vacia simplemente para poder llamarla, implementar su test y ejecutarlo comprobando que falla.

Para ello debemos de crear un nuevo fichero al que llamaremos por ejemplo myfactorial.py en el que definiremos dicha función y crearemos un fichero llamado test_.py donde crearemos nuestra función test_myfactorial() 


## Primeros pasos

### myfactorial.py
```python

def factorial(numero):
   return 0

```

### test_.py
```python

import pytest
import myfactorial

def test_myfactorial():
   assert myfactorial.factorial(3) == 6

```

Una vez hemos hecho esto debemos de implementar nuestra función encargada de calcular el factorial 
### myfactorial.py
```python

def factorial(numero):
   fact = 1
   for i in range(1,numero+1):
       fact = fact * i
   return fact

```
Una vez implementada debemos de abrir una terminal en ese mismo directorio y ejecutar el siguiente comando:

      pytest test_.py 

Y si todo ha ido bien obtendremos un resultado similar a este:

      ===================================== test session starts =====================================
      platform linux -- Python 3.8.5, pytest-6.2.3, py-1.10.0, pluggy-0.13.1
      rootdir: /home/marcos/Desktop/Curso
      collected 1 item                                                                              

      test_.py .                                                                              [100%]

      ====================================== 1 passed in 0.01s ======================================


Hecho esto ahora te toca a tí, implementa unos test que comprueben que pasa si queremos calcular el factorial de 0 y otros que comprueben que pasa si queremos calcular el factorial de un numero negativo. Observa los resultados y refactoriza la función si es necesario.