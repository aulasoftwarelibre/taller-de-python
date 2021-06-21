def uno():
    print("Enero")
 
def dos():
    print("Febrero")
 
def tres():
    print("Marzo")
 
def cuatro():
    print("Abril")
 
def cinco():
    print("Mayo")
 
def seis():
    print("Junio")
 
def siete():
    print("Julio")
 
def ocho():
    print("Agosto")
 
def nueve():
    print("Septiembre")
 
def diez():
    print("Octubre")
 
def once():
    print("Noviembre")
 
def doce():
    print("Diciembre")
 
 
# "main"
mes=int(input("Introduce un numero para obtener el mes que le corresponde: "))
switch = {
    1: uno,
    2: dos,
    3: tres,
    4: cuatro,
    5: cinco,
    6: seis,
    7: siete,
    8: ocho,
    9: nueve,
    10: diez,
    11: once,
    12: doce
}
# Obtiene la función del diccionario. 
# Si argument no se corresponde con ningún indice 
# func obtendrá la función lambda equivaliendo esto al default
func = switch.get(mes, lambda: print("No existe un mes equivalente al numero introducido"))
# Para ejecutar la función obtenida usamos:
func()

