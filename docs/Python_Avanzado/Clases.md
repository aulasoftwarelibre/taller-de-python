# Clases

La Programación Orientada a Objetos es un paradigma de programación que viene a innovar la forma de obtener resultados. Los objetos se utilizan como metáfora para emular las entidades reales del negocio a modelar.

Muchos de los objetos prediseñados de los lenguajes de programación actuales permiten la agrupación en bibliotecas o librerías, sin embargo, muchos de estos lenguajes permiten al usuario la creación de sus propias bibliotecas.

Está basada en varias técnicas del sexenio: herencia, cohesión, abstracción, polimorfismo, acoplamiento y encapsulamiento.

Su uso se popularizó a principios de la década de 1990 y en la actualidad resulta imprescindible para todo programador.

## ¿Como creamos una clase en Python?

Pues es muy sencillo ya que la sintaxis como siempre es muy similar a la de otros lenguajes. En este caso vamos a poner un ejemplo creando una clase persona de la que heredará la clase informático.

Y lo único que debemos de tener presente es que a diferencia de C++ que lo pone automáticamente en Python las funciones de la clase reciben como parámetro el objeto que las llama es por eso que ponermo (self). Sería equivalente al puntero this en C++.

```Python
class persona: #Clase persona
  
  nombre_ #Variable que almacena el nobre de la persona
  apellidos_ #Variable que almacena los apellidos_ de la persona
  altura_ #Variable que almacena la edad_ de la persona
  edad_ #Variable que almacena la edad_ de la persona
  
  def __init__(self, nombre, apellidos, altura, edad): #Constructor
   self.nombre_ = nombre
   self.apellidos_ = apellidos
   self.altura_ = altura
   self.edad_ = edad

  def getnombre(self): #Observador que devuelve el nombre_ de la persona
    return self.nombre_
  
  def getapellidos(self): #Observador que devuelve los apellidos_ de la persona
    return self.apellidos_
  
  def getaltura(self): #Observador que devuelve la altura_ de la persona
    return self.altura_
  
  def getedad(self): #Observador que devuelve el nombre_ de la persona
    return self.edad_

  def setnombre(self, nombre): #Modificador que permite cambiar el nombre_ de la persona
    self.nombre_ = nombre

  def setapellidos(self, apellidos): #Modificador que permite cambiar los apellidos_ de la persona
    self.apellidos_ = apellidos

  def setaltura(self, altura): #Modificador que permite cambiar la altura_ de la persona
    self.altura_ = altura

  def setedad(self, edad): #Modificador que permite cambiar la edad_ de la persona
    self.edad_ = edad

  def hablar(self): #Metodo de la clase
    return "Estoy hablando"
  
  def caminar(self): #Metodo de la clase
    return "Estoy caminando"
  
  def dormir(self): #Metodo de la clase
    return "zZz"


class Informatico(persona): # Informático hereda de forma pública de persona
  
  lenguajes_
  experiencia_
  
  def __init__(self, lenguajes, experiencia):
    self.lenguajes_ = lenguajes
    self.experiencia_ = experiencia

  def getLenguajes(self):
    return self.lenguajes_

  def aprender(self, lenguajes):
    self.lenguajes_ = lenguajes
    return self.lenguajes_

  def programar(self):
    return "Estoy programando"

  def repararPC(self):
    return "He reparado tu pc"

```