with open('quijote.txt', 'r') as file:
    datos = file.read()
    flag = False
    linea = 0
    for i in datos:
        if flag == False:
            if i != "\n":
                flag = True
                linea += 1
        if flag == True:
            if i == "\n":
                flag = False

    flag = False
    palabras = 0
    for i in datos:
        if flag == False:
            if i != " " or i != "\n":
                flag = True
                palabras += 1
        if flag == True:
            if i == " " or i == "\n":
                flag = False
    print(palabras)
    