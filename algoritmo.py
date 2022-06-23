def Separar(datos):

    lista = []
    for i in datos:

        lista.append(int(i))

    return(lista)

def removerespacios(lista):
    return lista.replace(' ','')


def maximos_Eventos(Inicio, final, ultimo, cantidad):

    sig_evento = ultimo + 1

    while sig_evento < cantidad and Inicio[sig_evento] < final[ultimo]:
        sig_evento = sig_evento + 1
    
    if sig_evento < cantidad:
        return [sig_evento] + maximos_Eventos(Inicio, final, sig_evento,cantidad)

    return []



cantidad_de_act = int(input("ingrese la cantidad de actividades: \n"))

#----------------------------------------------------------------------------------------

ini = input("ingrese los tiempos de inicio de las actividades: \n")


iniclean = removerespacios(ini)



iniciolista = Separar(iniclean)

#-----------------------------------------------------------------------------

fin = input("ingrese los tiempos de fin de las actividades: \n")


finclean = removerespacios(fin)

finlista = Separar(finclean)



valor = (maximos_Eventos(iniciolista,finlista,0,cantidad_de_act))

valor.insert(0,0)


print("las actividades que puede realizar la person son : \n",*valor)
