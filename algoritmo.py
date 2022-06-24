#la funcion separar tiene la tarea de tomar los numeros entregados en los horarios de inicio
#y los horarios de fin para combertilos en una lista y sea mas facil para nuestro algoritmo
#greedy tabajar con ella

def Separar(datos):    

    lista = []
    for i in datos:

        lista.append(int(i))

    return(lista)

#_-------------------------------------------------------------------------------------------------

#la función removerespacios hace lo que su nombre indica, en caso de que un usuario escriba en el
#input un numero con espacios. Esta función se encargará de eliminarlos para que la función
#separar no tenga conflictos.


def removerespacios(lista):
    return lista.replace(' ','')

#--------------------------------------------------------------------------------------------------

#la función maximos_eventos es la que se comporta como un algoritmo greedy para su uso necesitaremos
#4 parámetros:
# -los horarios de inicio 
# -los horarios de termino
# -el último número seleccionado de la lista, aunque este parámetro siempre partirá con 0
# -y la cantidad que es el largo de nuestra lista o de "actividades" 

# lo que hace esta función en el primer while es siempre seleccionar el evento que dure menos
# y luego de este while tenemos nuestra condición(if) que es la que dice que debemos seguir buscando
# los eventos que se demoren menos, pero ahora con la condición de que no pueden empezar antes
# de que termine el ultimo evento seleccionado.
# para finalmente retornarnos la lista con la solución optima.

def maximos_Eventos(Inicio, final, ultimo, cantidad):

    sig_evento = ultimo + 1

    while sig_evento < cantidad and Inicio[sig_evento] < final[ultimo]:
        sig_evento = sig_evento + 1
    
    if sig_evento < cantidad:
        return [sig_evento] + maximos_Eventos(Inicio, final, sig_evento,cantidad)

    return []

#-------------------------------------------------------------------------------------------

#este input nos pregunta la cantidad de actividades

cantidad_de_act = int(input("ingrese la cantidad de actividades: \n"))

#----------------------------------------------------------------------------------------
# estos 3 procesos se encargan de tener la lista de nuestros horarios de inicio.

ini = input("ingrese los tiempos de inicio de las actividades: \n")

iniclean = removerespacios(ini)

iniciolista = Separar(iniclean)

#-----------------------------------------------------------------------------------------
# estos 3 procesos hacen lo mismo que el anterior pero con la lista de los horarios de fin.

fin = input("ingrese los tiempos de fin de las actividades: \n")

finclean = removerespacios(fin)

finlista = Separar(finclean)

#------------------------------------------------------------------------------------------
#aca se esta haciendo uso de nuestra función greedy creada anteriormente.

valor = (maximos_Eventos(iniciolista,finlista,0,cantidad_de_act))

valor.insert(0,0)

print("las actividades que puede realizar la person son : \n",*valor)
