# Comentarios

Una de las cosas más importantes a la hora de programar son los comentarios. En Python como en otros muchos lenguajes existen distintos tipos de comentarios que usaremos en base al contexto y a nuestras necesidades. 

=== "Python"

    ```python
    # Esto mostrará el texto hola por la consola

    print("Hola")

    # Estas dos instrucciones muestran codigo por pantalla

    print("mundo")

    # print("!!")

    """
    Esto no se mostrará:
    print("Esto no se va a mostrar")
    print("Porque estará en dentro de un comentario multilinea")
    """

    print("Adios!!")
    ```

=== "C++"

    ```cpp
    #include <cstdio>
    #include <cstdlib>
    #include <iostream>
    using namespace std;

    int main()
    {
      //Esto mostrará el texto hola por la consola
      cout<<"Hola\n";

      //Estas dos instrucciones muestran código por pantalla

      cout<<"mundo\n";

      //cout<<"!!\n";

      /* 
      Esto no se mostrará:
      cout<<"Esto no se va a mostrar"
      cout<<"Porque estará dentro de un comentario multilinea"
      */

      cout<<"Adios!!\n";
      return 0;
    }
    ```
