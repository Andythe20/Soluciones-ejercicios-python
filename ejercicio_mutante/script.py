import csv
#Definir funciones
def promedioIMC_por_estado_de_salud (nombre_archivo, estado_salud):
    D = {} #diccionario para guardar datos de pacientes
    with open(nombre_archivo, 'r') as file:
        datos = csv.reader(file)
        for i in datos:
            linea = ''.join(i)
            linea = linea.split(';')
            if linea[0] == estado_salud:  #primero califico que la persona tenga el estado de salud que pido
                if linea[1] not in D:    #despues voy juntando el IMC por estado de salud
                    D[linea[1]] = []
                D[linea[1]].append(float(linea[-1]))

    #Calculo los promedios
    for i in D:
        D[i] = round(sum(D[i]) / len(D[i]), 2)

    a_imprimir= []
    for i in D:
        linea = [D[i], i]     #si pongo en el primer indice de la sublista un numero, el sort ordena de acuerdo al primer indice
        a_imprimir.append(linea)
    
    #Escribir archivo
    with open(estado_salud + '-IMC.txt', 'w') as file:
        for i in a_imprimir:
            linea = i[1] + ': ' + str(i[0]) + '\n'
            file.write(linea)


def estado_de_salud(nombre_archivo):
    d = {} #voy a crear un diccionario anidado, donde la primera llave sera el estado de salud, y dentro habrán dos llaves 'Yes' y 'No', 
           #donde cada una guardara una lista con la cantidad de yes y no, que corresponde si hace ejericio o no.

    with open(nombre_archivo, 'r') as file:
        datos = csv.reader(file)
        for i in datos:
            linea = ''.join(i)
            linea = linea.split(';')
            if linea[0] not in d: #agrego la primera llave 'estado de salud'
                d[linea[0]] = {}
            if linea[2] not in d[linea[0]]: #agrego la segunda llave 'YES' o 'NO'
                d[linea[0]][linea[2]] = []
            d[linea[0]][linea[2]].append(linea[2]) #agrego 'YES' o 'NO' a una lista asociada a la segunda llave

    for i in d:  #primero recorro el diccionario, con 'i' valiendo el estado de salud
        with open('estado_de_salud_' + i + '.txt', 'w') as file:
            for j in d[i]:  #recorro cada llave(estado de salud) la cual es un diccionario con llaves 'Yes' y 'No'
                if j == 'Yes':
                    linea = 'Exercise: ' + str(len(d[i][j])) + '\n'   #d[i][j] ---> corresponde a una lista llena con valores equivalentes a 'Yes' o 'No' dependiendo del valor de la llave
                    file.write(linea)                                 #y solo necesito el largo de esa lista
                else:
                    linea = 'No exercise: ' + str(len(d[i][j])) + '\n'
                    file.write(linea)

estado_de_salud('datos.csv')