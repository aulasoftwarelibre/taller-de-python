# Sintaxis

El funcionamiento de pytest es similar al de todas las librerías de testing. Esto lo podemos observar tanto en su sintaxis como en la forma de implementar los test. En este caso vamos ha hacer la comparativa entre gtest (el cual muchos de vosotros conocereis de la carrera) y pytest.

### Python

```python

assert Val1 == Val2   #¿Val1 igual Val2?
assert Val1 != Val2   #¿Val1 diferente Val2?
assert Val1 <  Val2   #¿Val1 menor que Val2?
assert Val1 <= Val2   #¿Val1 menor o igual que Val2?
assert Val1 >  Val2   #¿Val1 mayor que Val2?
assert Val1 >= Val2   #¿Val1 mayor o igual que Val2?
assert Val1 == TRUE   #¿Val1 igual TRUE?
assert Val1 == FALSE  #¿Val1 igual FALSE?

```

### C++

```cpp

EXPECT_EQ(val1,val2) //¿Val1 igual Val2?
EXPECT_NE(val1,val2) //¿Val1 distinto Val2?
EXPECT_LT(val1,val2) //¿Val1 menor que Val2?
EXPECT_LE(val1,val2) //¿Val1 menor o igual que Val2?
EXPECT_GT(val1,val2) //¿Val1 mayor que Val2?
EXPECT_GE(val1,val2) //¿Val1 mayor o igual que Val2?
EXPECT_TRUE(val1)    //¿Val1 igual que TRUE?
EXPECT_FALSE(val2)   //¿Val1 igual que FALSE?

```

Estas expresiones son las que debemos de utilizar en nuestros test cuando queramos comprobar el funcionamiento de nuestras funciones.

