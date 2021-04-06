# Pytest

![Pytest](https://pbs.twimg.com/media/EjI7ONtVgAIa4eW.png)

Lo primero que tenemos que hacer si queremos utilizar Pytest para testear nuestro código es instalarlo para ello abriremos una nueva terminal e introduciremos el siguiente comando. Tal y como se puede ver estamos haciendo uso de pip el gestor de paquetes de Python que previamente habíamos instalado. 

      pip install pytest

Una vez hecho esto podemos comprobar la versión que tenemos instalada escribiendo el siguiente comando:

      pytest --version

Y obtendríamos un resultado como este:

      This is pytest version 4.6.9, imported from /usr/lib/python2.7/dist-packages/pytest.pyc

Una vez lo hemos instalado y hemos comprobado la versión que tenemos llega la hora de empezar a realizar nuestros primeros test.

A la hora de escribir las pruebas es necesario que tanto los ficheros donde las vamos a escribir como las mismas funciones de prueba dentro del fichero comiencen con el prefijo test_ ya que si no cuando llamemos a pytest pasandole la ruta del directorio este no las encontrará. 

Un ejemplo de llamada a Pytest sería algo asi:

      pytest /home/marcos/Desktop/Curso

