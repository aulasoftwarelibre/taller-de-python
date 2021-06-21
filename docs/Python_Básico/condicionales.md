# Condicionales

Conforme vayamos avanzando nuestros programas serán cada vez más complicados y es posible que necesitemos hacer uso de estructuras condicionales que nos permitan direccionar ejecutar determinadas secciones de nuestro codigo si se cumplen determinadas condiciones. Para ello haremos uso de las estructuras condicionales que en Python son las siguientes:

=== "Python"

    ```python

    if expression:
        code

    elif expression:
        code

    else:
        code

    expression1 if condition else expression2 #Operador ternario

    ```

=== "C++"

    ```cpp
    if ( condition )
    {
        code 
    }

    else if ( condition )
    {
        code 
    }

    else
    {
        code 
    }

    condition ? expression1 : expression1; //Operador ternario

    switch (expression)
    {
        case  constant-expression :
            code 
        break;

        default:
        break;
    }
    ```

Podemos observar que en ambos lenguajes tenemos las mismas estructuras aunque en C++ además podemos hacer uso de la estructura Switch que en Python no está incluida. Pese a que se considera un antipatrón, podría implementarse en Python haciendo uso de los diccionarios:


```python

# "main"
mes = int(input("Introduce un numero para obtener el mes que le corresponde:"))
nombres_meses = {
    1: "Enero",
    2: "Febrero",
    3: "Marzo",
    4: "Abril",
    5: "Mayo",
    6: "Junio",
    7: "Julio",
    8: "Agosto",
    9: "Septiembre",
    10: "Octubre",
    11: "Noviembre",
    12: "Diciembre"
}
print(nombres_meses.get(mes, "No existe un mes equivalente al número introducido"))
```

!!! tip "Ojo"
    En el ejemplo anterior, hemos usado `#!python nombres_meses.get(mes, valor)` en lugar de `#!python nombres_meses[mes]`. La función `get` nos permite dar un valor *por defecto*, en caso de que la clave no exista en el diccionario.
    
    Por ejemplo, si el usuario introduce el valor `#!python 14`, `#!python nombres_meses[14]` dará un error que terminará el programa.
