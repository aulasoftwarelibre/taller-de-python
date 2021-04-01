# Copiado de objetos: `copy`

[Documentación](https://docs.python.org/3/library/copy.html)

En Python, por defecto, todos los valores son *referencias* a un objeto. Si copiamos una referencia a un objeto *mutable* (es decir, que puede ser modificado), por ejemplo una lista, ambas copias se refieren a la misma lista. Por ejemplo:
```python
a = ['hola', 'adios', 'buenas']
b = a  # Copiamos la referencia, NO SE HACE COPIA
b[0] = 'hastaluego'  # Estamos modificando la lista original
print(a)
# >> ['hastaluego', 'adios', 'buenas']
print(b)
# >> ['hastaluego', 'adios', 'buenas']
```

Si, por algún motivo, necesitamos tener copias independientes, podemos hacer copias usando el módulo `copy`:
```python
import copy

a = ['hola', 'adios', 'buenas']
b = copy.copy(a)  # Creamos una copia de la lista
b[0] = 'hastaluego'  # Estamos modificando la copia
print(a)
# >> ['hola', 'adios', 'buenas']
print(b)
# >> ['hastaluego', 'adios', 'buenas']
```

¡Mucho ojo con objetos anidados! En el siguiente ejemplo tenemos una *lista de listas*. Si simplemente copiamos la lista externa, ambas listas contienen referencias a las mismas listas.
```python
a = [[1, 2], [3, 4], [5, 6]]
b = copy.copy(a)  # Copiamos las referencias, pero apunta a las mismas listas
b[0][1] = 10  # Ojo, estamos cambiando la primera lista
print(a)
# >> [[1, 10], [3, 4], [5, 6]]
```

!!! question inline end "Ejercicio"
    Un buen ejercicio para practicar el pensamiento recursivo es implementar una función de copia profunda (equivalente a `copy.deepcopy()`) usando únicamente la función de copia `copy.copy()`. ¡Inténtalo!

Si esto no es lo que queremos, tenemos que hacer una *copia profunda* o "deep copy" (es decir, ¡una copia recursiva!):
```python
a = [[1, 2], [3, 4], [5, 6]]
b = copy.deepcopy(a)
b[0][1] = 10
print(a)
# >> [[1, 2], [3, 4], [5, 6]]
print(b)
# >> [[1, 10], [3, 4], [5, 6]]
```
