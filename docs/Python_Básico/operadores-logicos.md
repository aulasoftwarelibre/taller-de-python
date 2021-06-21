# Operadores Lógicos

También debemos de conocer el funcionamiento de los operadores lógicos ya que son imprescindibles para poder implementar condiciones lógicas que guíen el flujo de control de nuestro programa

=== "Python"

    ```python
    # ¿igual?
    3 == 2  # = False

    # ¿menor que?
    3 < 2  # = False

    # ¿mayor que?
    3 > 2  # = True

    # ¿menor o igual que?
    3 <= 3  # = True

    # ¿mayor o igual que?
    3 >= 2  # = True

    # ¿diferente?
    3 != 2  # = True

    # Negación lógica (invertir el valor booleano)
    not (3 != 2)  # = False

    # Conjunción lógica / operador AND
    # True si y solo si ambos operandos son True
    (3 > 2) and (3 != 0)  # = True

    # Disyunción lógica / operador OR
    # True si alguno de los operandos es True
    (3 < 2) or (3 != 0)  # = True
    ```

=== "C++"

    ```cpp
    /*
    < ¿menor que?
    > ¿mayor que?
    <= ¿menor o igual que?
    >= ¿mayor o igual que?
    == ¿igual?
    != ¿diferente?
    ! Negación lógica (invertir el valor booleano)
    && Conjunción lógica / operador AND
    || Disyunción lógica / operador OR
    */
    ```
