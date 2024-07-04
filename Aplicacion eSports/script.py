from tabulate import tabulate

#Funciones
def mostrarmenu():
    print('''
    1. Registrar puntajes de torneo
    2. Listar todos los puntajes
    3. Imprimir por tipo
    4. Salir del programa
    ''')

def registrar_puntajes():
    tipo_jugador = input("Indique el tipo de jugador (Principiante, Avanzado, Experto): ")
    valorant = input("¿Desea ingresar puntaje en Valorant?(si/no): ")
    if valorant.lower() == 'si':
        puntaje_valorant = int(input("Puntaje Valorant: "))
    else:
        puntaje_valorant = 0
    fortnite = input("¿Desea ingresar puntaje en Fortnite?(si/no): ")
    if fortnite.lower() == 'si':
        puntaje_fornite = int(input("Puntaje Fortnite: "))
    else:
        puntaje_fornite = 0
    fifa = input("¿Desea ingresar puntaje en Fifa?(si/no): ")
    if fifa.lower() == 'si':
        puntaje_fifa = int(input("Puntaje Fifa: "))
    else:
        puntaje_fifa = 0
    datos.append([id, nombreyapellido, puntaje_valorant, puntaje_fornite, puntaje_fifa, tipo_jugador])

#Main
datos = []
while True:
    mostrarmenu()
    op = input("Ingrese una opción: ")
    if op == '4':
        break
    elif op == "1":
        try:
            id = int(input("ID Jugador: "))
        except:
            print("Ingrese ID numérico")
            continue
        nombreyapellido = input("Nombre y apellido: ")
        registrar_puntajes()
    elif op == '2':
        print(tabulate(datos, headers=['Id jugador', 'Nombre y apellido', 'Valorant', 'Fortnite', 'Fifa', 'Tipo']))
    elif op == '3':
        tipo = input("Indique el tipo de jugador (Principiante, Avanzado, Experto): ")
        datos_por_tipo = []
        with open(tipo + '.txt', 'w') as file:
            for i in datos:
                if i[-1].lower() == tipo.lower():
                    datos_por_tipo.append(i)
            file.write(tabulate(datos_por_tipo, headers=['Id jugador', 'Nombre y apellido', 'Valorant', 'Fortnite', 'Fifa', 'Tipo']))