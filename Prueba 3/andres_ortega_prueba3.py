import csv

#Funciones
def mostrarmenu():  #Menu principal
    print('''
    ***MENU PRINCIPAL***
    1. Filtro jugador
    2. Filtro precio
    3. Filtro consola y año
    4. Escribir archivo
    5. Salir
    ''')

def menuconsolas():   #menu para mostrar consolas disponibles 
    print('''
    Consolas disponibles:
        - Nintendo DS
        - Nintendo Wii
        - PlayStation3
        - Sony PSP
        - X360
        ''')

def menu_escribir_archivo():   #menu para elegir que filtro escribir
    print('''
    ***MENU ESCRITURA
    1. Escribir filtro jugador
    2. Escribir filtro precio
    3. Escribir filtro consola y año
          ''')

def filtro_jugador(filtro):
    global datos_jugador  #declaro una variable de tipo lista como global para ir actualizando las listas dependiendo de que filtro ingresen
                          #primero leo el archivo para extraer los datos por filtro
    filtro_datos = []
    with open('juegos.csv', 'r') as file:
        data = csv.reader(file)
        for i in data:
            if i[1] == filtro:  #aplico filtro (s/m)
                filtro_datos.append(i[0])
            if len(filtro_datos) == 10:
                break
        datos_jugador = filtro_datos

def filtro_precio(precio_min, precio_max):
    global datos_precio   #declaro una variable de tipo lista como global para ir actualizando las listas dependiendo de que filtro ingresen
                        #primero leo el archivo para extraer los datos por filtro
    filtro_datos = []
    with open('juegos.csv', 'r') as file:
        data = csv.reader(file)
        for i in data:
            if float(i[2]) > precio_min and float(i[2]) < precio_max : #aplico filtro si el precio esta dentro de los precios definidos
                filtro_datos.append(i[0])
            if len(filtro_datos) == 10:
                break
        datos_precio = filtro_datos
        
def filtro_consola_año(cons, year):
    global datos_consola_año    #declaro una variable de tipo lista como global para ir actualizando las listas dependiendo de que filtro ingresen
                                #primero leo el archivo para extraer los datos por filtro
    filtro_datos = []
    with open('juegos.csv', 'r') as file:
        data = csv.reader(file)
        for i in data:
            if cons.lower() == i[-2].lower() and year == int(i[-1]): #aplico filtro si coincide la consola y el año
                filtro_datos.append(i[0])
            if len(filtro_datos) == 10:
                break
        filtro_datos.sort() #ordeno alfabeticamente
        datos_consola_año = filtro_datos

def escribir_archivo(lista):
    with open('filtro_juegos.txt', 'w') as file:
        for i in lista:
            linea = ''.join(i) + '\n'   #recorro la lista, agrupo los datos y realizo salto de linea
            file.write(linea)

#Main

#listas que guardan datos segun los filtros realizados
datos_jugador = []
datos_precio = []
datos_consola_año = []
while True:
    mostrarmenu()
    op = input("Ingrese opcion: ")
    if op == "5":
        print("Saliendo del sistema")
        break
    elif op == '1':
        jugador = input('Singleplayer o Multiplayer (s/m)?: ')
        if jugador == 'm':  #multiplayer = 2 (2 jugadores)
            filtro_jugador('2')
        elif jugador == 's': #singleplayer = 1 (1 jugador)
            filtro_jugador('1')
        print("El resultado de la busqueda es(los 10 primeros):\n", datos_jugador)
    elif op == '2':
        min = float(input("Ingrese precio minimo: "))
        max = float(input("Ingrese precio maximo: "))
        filtro_precio(min, max)
        if len(datos_precio) == 0:
            print("No hay juego en ese rango de precios")
        else:
            print("El resultado de la busqueda es (los 10 primeros):\n", datos_precio)
    elif op == '3':
        menuconsolas()
        consola = input("Ingrese un tipo de consola: ")
        año = int(input("Ingrese año de lanzamiento: "))
        filtro_consola_año(consola, año)
        if len(datos_consola_año) == 0:
            print("No hay juegos con esos filtros")
        else:
            print("El resultado de la busqueda es (los 10 primeros):\n", datos_consola_año)
    elif op == '4':
        menu_escribir_archivo()
        op2 = int(input("Ingrese opcion: "))
        if op2 == 1:  #escribir con el filtro jugador
            if len(datos_jugador) == 0:
                print("No hay informacion que escribir")
            else:
                escribir_archivo(datos_jugador)
                print("Archivo creado!!!")
        elif op2 == 2: #escribir con el filtro precio
            if len(datos_precio) == 0:
                print("No hay informacion que escribir")
            else:
                escribir_archivo(datos_precio)
                print("Archivo creado!!!")
        elif op2 == 3: #escribir con el filtro consola y año 
            if len(datos_consola_año) == 0:
                print("No hay informacion que escribir")
            else:
                escribir_archivo(datos_consola_año)
                print("Archivo creado!!!")
