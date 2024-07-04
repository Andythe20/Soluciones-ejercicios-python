#Funciones
def totales_auto(patente):
    #leer archivo de viajes
    datos_por_patente = []  #lista para juntar la informacion por patente
    total = 0 #acumulador para juntar el dinero que realizo en los viajes
    promedio = 0 #acumulador para promediar el puntaje del viaje
    c = 0 #contador para saber cuanto dividir el promedio
    with open('viajes.txt', 'r') as file:
        txt = file.read()
        datos = txt.split('\n')  #primero separo los datos por patente
        for i in datos:
            linea = i.split('/')  #linea[0] guarda la patente
            linea2 = linea[1].split('-') #linea2 guarda los otros datos
            juntar = [linea[0]] + linea2 #junto los datos que tengo por patente
            datos_por_patente.append(juntar) #los guardo en la lista 'datos_por_patente'
        #revisar viajes de la patente y acumular el dinero
        for i in datos_por_patente:
            if patente == i[0]:
                c +=1
                total += int(i[1])
                promedio += float(i[3])
    if total == 0:    #significa que no hubo viaje, no puede haber una tarifa de valor 0
        print("Patente sin viajes")
    else:
        promedio = promedio / c
        #leer archivo de usuarios y detectar los que tomaron un viaje con la patente
        datos_por_usuario = [] #lista para juntar informacion por usuario
        with open('usuarios.txt', 'r') as file:
            txt = file.read()
            datos = txt.split('\n') #separo datos por usuario 
            for i in datos:
                linea = i.split('-') #separo datos del usuario
                datos_por_usuario.append(linea) #guardo los datos en la lista 'datos_por_usuario'
            #revisar match entre el codigo del usuario y con el viaje realizado por la patente
            nombres = []  #lista para guardar los nombres que tomaron viaje con la patente
            for i in datos_por_patente:
                if i[0] == patente:   #si la patente ingresada es igual a la patente que está guardada en la lista de datos por patente, recien verifico los codigos de usuario
                    for j in datos_por_usuario:
                        if i[2] == j[0]:
                            nombres.append(j[1])
            nombres = '-'.join(nombres)  #junto los nombres
            #escribir el archivo de la patente pedida
            datos_a_escribir = str(total) + '-' + nombres + '\nPuntaje promedio:' + str(promedio) #junto los datos que piden escribir
            with open('total_' + patente + '.txt', 'w') as file:
                file.write(datos_a_escribir)
totales_auto('MZ8843')
totales_auto('AA8888')
totales_auto('TY9844')
