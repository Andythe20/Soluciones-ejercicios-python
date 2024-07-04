import csv
#FUNCIONES
def menu():
    print('''   
    1. Grabar
    2. Buscar
    3. Guardar archivos
    4. Salir
''')
    
def verificar_nif(nif):
    if '-' not in nif:
        return False
    elif len(nif) != 12:
        return False
    elif nif[-4] != '-':
        return False
    else:
        p1, p2 = nif.split('-')  #dos variables que toman el primer y el segundo corte del split
        if len(p1) != 8:
            return False
        try:
            int(p1)
            return True    #p1 equivale a la parte numerica del nif, si no puede ejercutar int(nif)
        except:            #significa que el nif ingresado es inválido
            return False

def verificar_nombre(n):
    if len(n) < 8:
        return False
    c = 0        #false si tiene 2 espacios un nombre, ya que solo es nombre y apellido separado
    for i in n:
        if i == " ":
            c+=1
    if c != 1:
        return False
    else:
        try: #si el espacio esta correctamente posicionado
            p1, p2 = n.split(' ')
        except:
            return False
        return True

def buscar_nif(nif):
    if nif not in datos_por_nif:
        return False
    else:
        for i in datos_por_nif:
            if i == nif:
                return f'Nombre: {datos_por_nif[i][0]}\nEdad: {datos_por_nif[i][1]}'

def crear_archivo():
    #Verifico el rango de edad que existe en el diccionario, ademas de guardar los nombres para ordenarlos alfabéticamente
    menor = None
    mayor = 0
    nombre = []
    for i in datos_por_nif:
        nombre.append(datos_por_nif[i][0])
        if menor == None:
            menor = datos_por_nif[i][1]
        elif datos_por_nif[i][1] < menor:
            menor = datos_por_nif[i][1]
        elif datos_por_nif[i][1] > mayor:
            mayor = datos_por_nif[i][1]
    nombre.sort()
    
    #Escribir el archivo
    with open('edades_entre_' + str(menor) + '_y_' + str(mayor) + '.csv' , 'w', newline='') as file:
        escritor = csv.writer(file)
        for i in nombre:
            for j in datos_por_nif:
                if i == datos_por_nif[j][0]:
                    escritor.writerow([j, datos_por_nif[j][0], datos_por_nif[j][1]])

#MAIN
datos_por_nif = {}
while True:
    menu()
    op = input("Ingrese una opción: ")
    if op == "4":
        print("Hasta luego")
        break
    elif op == "1":
        while True:
            try:
                edad = int(input("Ingrese su edad: "))
            except ValueError:
                print("Ingrese su edad en formato numérico")
                continue
            if edad < 15:
                print("Debe ser mayor de 15 años")
                break
            else:
                nif = input("Ingrese su NIF: ")
                retornonif = verificar_nif(nif)
                if retornonif == False:
                    print("NIF ingresado incorrecto")
                else:
                    nombre = input("Ingrese nombre: ")
                    retornonombre = verificar_nombre(nombre)
                    if retornonombre == False:
                        print("Nombre ingresado inválido")
                        break
                    else:
                        print("Datos ingresados y guardados correctamente ")
                        datos_por_nif[nif] = [nombre, edad]
                        break
    elif op == "2":
        buscarnif = input("Ingrese el NIF a buscar: ")
        retornobuscar = buscar_nif(buscarnif)
        if retornobuscar == False:
            print("NIF no encontrado")
        else:
            print(retornobuscar)
    elif op == '3':
        crear_archivo()
