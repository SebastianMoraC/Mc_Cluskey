import os

def crear_matriz(matriz, columnas, filas):  # Funcion que crea matrices
    for i in range(filas):
        matriz.append([])
        for j in range(columnas):
            if j == 0:
                matriz[i].append(i)
            else:
                matriz[i].append(0)
    return matriz

def crear_matriz2(matriz, columnas, filas):  # Funcion que crea matrices
    for i in range(filas):
        matriz.append([])
        for j in range(columnas):
            matriz[i].append(0)
    return matriz

def dibujar_matriz(matriz, columnas, filas):  # Funcion que dibuja matrices

    for i in range(filas):
        for j in range(columnas):
            print(matriz[i][j], end="")  # El end se utiliza para que no se haga cambio de linea al imprimir en pantalla
        print("")  # Con esta linea hago el cambio de columna

def llenar_matriz(filas, columnas, matriz):  # Esta funcion llena las matrices de ceros y unos
    cantidad = filas // 2
    repeticiones = 1
    iteracion = 0

    for c in range(1, columnas):  # recorre cada columna
        for i in range(repeticiones):  # realiza la cantidad de repeticiones correspondientes a cada columna

            for a in range(cantidad):  # coloca la cantidad correspondiente de cada 0 por cada repeticion
                matriz[iteracion][c] = 0
                iteracion = iteracion + 1  # La iteraccion me indica que fila irá el numero
            for b in range(cantidad):  # coloca la cantidad correspondiente de cada 1 por cada repeticion
                matriz[iteracion][c] = 1
                iteracion = iteracion + 1
        repeticiones = repeticiones * 2  # aumenta la cantidad de repeticiones en cada fila
        cantidad = cantidad // 2  # Divide la cantidad de 0 y 1 que entraran
        iteracion = 0
    return matriz

def minterms(matriz, filas, lista):
    matriz_nueva = []
    iteracion = 0
    print(
        "--------------------------------------------------------------------------------------------------------------------")
    print("Ingrese el numero -1 cuando quiera finalizar de ingresar numeros, los numeros deben estar entre: [0-",
          filas - 1, "]")
    # for i in range(filas):
    while iteracion < filas:
        valor = int(input("Ingrese el minterm: "))
        if valor <= filas - 1:
            if valor != -1:
                matriz_nueva.append(matriz[valor])
                lista.append(valor)
                iteracion += 1
            else:
                break
        else:
            print("INGRESE UN NUMERO ENTRE: [0-", filas - 1, "]")
    return (matriz_nueva)

def EMCclauskey(matriz, variables):  # se ordenan los valores binarios por cantidad de unos presentes
    Mcclauskey = list()  # lista final donde estara la agrupacion por unos
    tempcombinaciones = list()  # lista temporal donde se almacenara cada grupo de unos
    tempcombinacion = list()
    tempdecimal = list()  # lista para los valores decimales Nota: en primera instancia sera un unico valor pereo mientras se ejecuta el rpoceso de mclauskey se obtendran mas valores
    n1 = list()

    iteracion = 0  # se itera la cantidad de variables que hay iniciando desde 0
    flag = 0  # una bandera para saber si existen agrupaciones de unos adecuadas para guardas
    while iteracion <= variables:  # se utilizara como control para que se guarden los valores por cantidad de unos
        for a in range(len(matriz)):  # se reorre primero por cada fila
            flag = 0
            count = 0  # contador de unos
            t = range(1, variables)  # por cuestiones de funcionamiento es necesario esta asignacion
            for b in t:  # recorre por columnas, se empieza desde la posicion 1 por el hehcho de que en la primera posicion esta  el numero representado en decimal
                if matriz[a][b] == 1:  # condicional para contar
                    count += 1
                tempcombinacion.append(matriz[a][b])  # se guarda la combinacion binaria
                # como #"$"!#"$!#!$ se borra toda una fila de la matriz?"
            if count == iteracion:  # se verifica si la cantidad de unso coincide con la cantidad que se esta trabajando actualmente
                flag = 1
                tempdecimal.append(matriz[a][0])  # se guarda el decimal
                n1.append(tempcombinacion)
                n1.append(tempdecimal)
                n1.append(0)
                tempcombinaciones.append(n1)  # finalmente se guarda la combinacion de binarios en una lista

            n1 = []
            tempcombinacion = []  # se vacia la lista para evitar ambiguedad
            tempdecimal = []

        if tempcombinaciones != []:
            Mcclauskey.append(tempcombinaciones)  # finalmente se guarda la lista de binarios en una lista

        tempcombinaciones = []
        iteracion += 1  # aumenta la iteraion con el fin de comprobar todas las cantidades de unos
    return Mcclauskey

def ecuacion(Matriz):  # se imprime la ecuacion
    Leters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M",
              "N"]  # letras para representar las variables
    # print(Matriz[1])
    for a in Matriz:  # se recorre la matriz
        if a == Matriz[-1]:
            for b in range(len(a[0])):
                if a[0][b] == 1:
                    print(Leters[b], end="")
                if a[0][b] == 0:
                    print("not(" + Leters[b] + ")", end="")
        else:
            for b in range(len(a[0])):
                if a[0][b] == 1:
                    print(Leters[b], end="")
                if a[0][b] == 0:
                    print("not(" + Leters[b] + ")", end="")
            print(" + ", end="")

def reduccion(matrices, implicantes):  # se reducen los valores que poseen la misma ecuacion
    tempresult =list()
    result = list()  # resultado de eliminar todos los elementos repetidos
    termino = 0  # entero para saber la cantidad de terminos revisados
    previous = list()
    temp_decimal = list()
    for ini in range(len(matrices)):  # se recorre la matriz
        termino = 0
        for a in range(len(matrices[ini])):  # se recorre cada agrupacion de unos
            if len(matrices[ini]) == 1:  # se consulta si hay un unico elemento en la grupacion de unos
                tempresult.append(matrices[ini][a])  # se grega la combinacion binario y sus valores decimales
            if a + 1 >= len(matrices[ini]):  # en caso de que no hayan mas se cierra el ciclo
                break
            temp1 = ((matrices[ini])[a])  # se toma un elemento de la lista
            temp2 = ((matrices[ini])[a + 1]) # se toma el elemento siguiente en la lista

            if temp1[0] == temp2[0]: # en caso de que sean iguales los binarios
                for b in temp2[1]: # en caso tal de que hayan valores en una combinacion binaria y en la otra que es exactamente igual se extraen para proximamente ser agregada en la parte siguiente 
                    if not(b in temp1[1]):
                        temp_decimal.append(b)
                if not (temp_decimal == []): # en caso de que no este vacio
                    for c in temp_decimal:
                        temp1[1].append(c)
                    temp_decimal = []
                if termino <= 0:
                    tempresult.append(temp1)
                    termino = 1
                    previous = temp1
                    temp1 = []
                    temp2 = []
                    temp_decimal=[]
                else:
                    temp_decimal = temp1
                    for d in temp2[1]:
                        if not (b in temp1[1]):
                            temp_decimal.append(d)
                    if not (temp_decimal == []):
                        for e in temp_decimal[1]:
                            if not(e in (tempresult[termino - 1])[1]):
                                (tempresult[termino - 1])[1].append(e)
                    temp_decimal=[]
            elif temp2[0] != temp1[0]: # en caso tal de que no se 
                if termino <= 0:
                    tempresult.append(temp1)
                    termino += 1
                    tempresult.append(temp2)
                    termino += 1
                    temp1 = []
                    temp2 = []
                else:
                    tempresult.append(temp2)
                    termino += 1
                    temp2=[]

    count=0
    for z1 in tempresult :
        for a in range(1,len(tempresult)):
            if z1[0] != (tempresult[a])[0]:
                count=0
            else:
                count=1
        if count == 0:
            result.append(z1)
            
    for z in implicantes:
        result.append(z)

    return result

def revision(a, b):  # se confirma se exactamente cambia un bit entre los dos binarios en cuestion
    counte = 0

    for i in range(len(a)):  # se va a recorrer de extremo a extremo cada binario
        if not (a[i] == b[i]):  # se consulta si hay presente un cambio entre los dos bits en cuestion
            counte += 1  # en caso tal se cuenta la cantidad de cambios
    if counte == 1:
        return True  # si solo existe un cambio de un solo bit se podra proceder a la mezcla
    else:
        return False  # en caso contraio no se podra ejecutar la mezcla

def comparacionMC(
        MCclauskey):  # se realiza las comparaciones entre cada grupo de binarios hasta que no hayan combinaciones posibles devolviendo los binarios corresponidntes a la ecuacion
    Mcclauskeycomplete = list()  # matriz que contendra las agrupaciones de las combinaciones resultantes
    tempMcclauskeycomplete = list()
    tempcombinaciones = list()  # lista que tendra temporalmente cada agrupacion
    implicantes = list()  # se guardaran todas las combinaciones binarias que no se mexclaron en algun punto o

    templist1 = list()  # lista para tomar una agrupacion
    templist2 = list()  # lista para tomar la siguiente agrupacion
    ni = list()  # lista de decimal combiancion binaria y validacion
    combinaciones = bool()

    fin = 0
    while fin != 1:
        i = 0
        while len(MCclauskey) > i + 1:  # comenzamos a sacar cada agrupacion de 1
            templist1 = MCclauskey[i]  # tomamos una agrupacion de unos
            templist2 = MCclauskey[i + 1]  # y luego tomamos la siguiente agrupacion

            for a in templist1:  # e comienza a recorrer la primera agrupacion con le fin de sacar una elemento y compararlos con todos los de la agrupacion siguiente
                for b in templist2:  # se recorre la segunda agrupacion para compararla completamente con el elemento de sacado anteiormente
                    if ((
                            (a[0].count(1) + 1 == b[0].count(1)) or
                            (a[0].count(1) == b[0].count(1) + 1) or
                            ((a[0].count(1) + 1 == b[0].count(1)) and (a[0].count('-') == b[0].count('-'))) or
                            ((a[0].count(1) == b[0].count(1)) and (a[0].count('-') + 1 == b[0].count('-'))) or
                            ((a[0].count(1) == b[0].count(1) + 1) and (a[0].count('-') == b[0].count('-'))) or
                            ((a[0].count(1) == b[0].count(1)) and (a[0].count('-') == b[0].count('-') + 1))
                    ) and revision(a[0], b[0]) == True
                    ):  # se consulta si estos dos elemetos tienen un bit de diferencia
                        tempbinary = list()  # esta variable temporal se encargara de solamente guardar el binario
                        tempdecimal = list()
                        for c in range(len(a[
                                               0])):  # se comienzan a recorrer ambos elementos con el fin de encontrar la posicion donde se encuentra el uno en comun
                            if (a[0])[c] != (b[0])[
                                c]:  # se consulta si precisamente la posisicon en cuestion contiene el cambio de bit
                                tempbinary.append('-')  # se registra el cambio de bit
                            else:
                                tempbinary.append((a[0])[c])  # si no se guarda la posicion normal
                        for d in range(len(a[1])):  # se guarda el decimal del primer inplicante
                            tempdecimal.append((a[1])[d])
                        for d in range(len(b[1])):  # se guarda el decimal del segundo inplicante
                            tempdecimal.append((b[1])[d])

                        ni.append(tempbinary)
                        ni.append(tempdecimal)
                        ni.append(
                            0)  # en las 3 anteriores lineas se crea la tupla que contiene la lista de decimales que formaron el binario en cuestion y un int de validacion para saber si se mexcla o no
                        tempbinary = []  # se vacia con el fin de evitar redundancia
                        tempdecimal = []
                        tempcombinaciones.append(ni)  # se guarda en la agripacion correspondiente
                        ni = []
                        b[2] = 1  # se cambia la posicion de la validacion para saber que fue mezclado
                        a[2] = 1
            if tempcombinaciones != []:
                tempMcclauskeycomplete.append(
                    tempcombinaciones)  # se guarda las agrupaciones y se procede a los siguiente grupo
            tempcombinaciones = []
            i += 1
        comprobaciondefin = 0  # se utilizara para saber si se mezclo algun elemento

        if len(tempMcclauskeycomplete) == 0:  # condicional para saber el fin del proceso
            if not (len(Mcclauskeycomplete) == 0):  # condicional para saber si no hubo combinacion
                combinaciones = True
                break
            else:
                combinaciones = False  # si no hay combinacion alguna

        for a in MCclauskey:  # se recorre cada lista
            for b in a:  # se recorres cada binario
                if b[2] == 0:  # en caso tal de que la validacion de mezcla sea 0
                    implicantes.append(b)  # dicho elelemtno pasa a ser un implicante
                    comprobaciondefin += 1  # se cuenta cuantos elementos no fueron mezclados

        elementos = 0
        for a in MCclauskey:  # se cuenta el total de binarios en la matriz
            elementos += len(a)

        if (len(MCclauskey) == 1) or (
                elementos == comprobaciondefin):  # en caso tal de que solo haya una sola lista o ninguno de los elementos de la lista se haya podido mezclar se finaliza
            fin = 1
            break

        MCclauskey = []
        for a in tempMcclauskeycomplete:
            MCclauskey.append(a)

        Mcclauskeycomplete.append(tempMcclauskeycomplete)
        tempMcclauskeycomplete = []
    # ec=list()
    # ec=ecuacion(Mcclauskeycomplete[-1],implicantes)
    if combinaciones == True:
        solutions = list()
        solutions = reduccion(Mcclauskeycomplete[-1], implicantes)
    else:
        solutions = list()
        solutions = reduccion(MCclauskey, [])

    return solutions

def llenar_verificacion(ecuacion, minterms):
    matriz1=crear_matriz2([],len(minterms)+1,len(ecuacion)+1)
    contador=0
    for i in range(len(ecuacion)):
        matriz1[i+1][0]=ecuacion[i]
    for i in range (len(minterms)):
        matriz1[0][i+1]=minterms[i]
    for k in range(len(ecuacion)):

        for i in range (len(minterms)):
            while (contador <= ((len(ecuacion[k][1]))-1)):
                if(matriz1[0][i+1]==ecuacion[k][1][contador]):
                    matriz1[k+1][i+1]=1
                contador=contador+1

            contador=0
    return matriz1

def rellenar2(matriz,columna,filas):
    for i in range(1,filas):
        if(matriz[i][columna]==1 or matriz[i][columna]==2 ):
            matriz[i][columna]=2
    return matriz

def rellenar(matriz,fila_uno,columnas,columna,filas):
    for i in range(1,columnas):
        if(matriz[fila_uno][i]==1 or matriz[fila_uno][i]==2 ):
            matriz[fila_uno][i]=2
            matriz=rellenar2(matriz,i,filas)

def rellenar3(matriz,fila_uno,columnas,columna,filas):
    for i in range(1,columnas):
        if(matriz[fila_uno][i]==1 or matriz[fila_uno][i]==2 ):
            matriz[fila_uno][i]=2
            matriz=rellenar4(matriz,i,filas)

def rellenar4(matriz,columna,filas):
    for i in range(filas):
        if(matriz[i][columna]==1 or matriz[i][columna]==2 ):
            matriz[i][columna]=2
    return matriz

def analisis(matriz,ecuacion_final,columnas,filas):
    matriz_nueva=[]
    s=0
    for i in range(1,filas):
        if(matriz[i].count(1) != 0):
            matriz_nueva.append(matriz[i])
            s+=1
    if(s>1):
        ecuacion_final=contar(matriz_nueva,ecuacion_final,len(matriz_nueva),len(matriz_nueva[0]))

    return ecuacion_final

def calcular_mayor(matriz):
    mayor = matriz[0][0]
    mayor2=0
    for i in range(len(matriz)):
        menor=matriz[i][0]
        if (menor > mayor):
            #print(menor)
            mayor = matriz[i][0]
            mayor2=i

    return matriz[mayor2][1]

def contar(matriz,ecuacion_final,filas,columnas):
    matriz_nueva=[]
    s=0
    for i in range(filas):
        matriz_nueva.append([matriz[i].count(1)])
        matriz_nueva[s].append(i)
        s+=1

    mayor=calcular_mayor(matriz_nueva)
    ecuacion_final.append(matriz[mayor][0])
    rellenar3(matriz,mayor,columnas,0,filas)
    matriz.pop(mayor)

    for l in range(len(matriz)-1):
        if(matriz[l].count(1)==0):
            matriz.pop(l)
    #print("-------------------")
    #print(matriz)
    #print("-------------------")
    #if (len(matriz) == 1 or len(matriz)==2):
    #    ecuacion_final.append(matriz[0][0])
    if(mayor==calcular_mayor(matriz) and len(matriz)>1):
            contar(matriz,ecuacion_final,columnas,len(matriz)-1)
    else:
        for p in range(len(matriz)-1):
            ecuacion_final.append(matriz[p][0])
    return ecuacion_final

def verificacion(matriz,columnas,filas):
    contador=1
    i=1
    unos=0
    fila_uno=0
    ecuacion_final=[]
    repetido=0
    repetido2=0
    #print(filas)
    #print(matriz[1][0]) # primero fila , segundo columna
    #for i in range (1,columnas):
    while(i<columnas):#i = 1
        while(contador<filas): #contador = 1  #filas=4
            if(matriz[contador][i]==1 or matriz[contador][i]==2):
                fila_uno=contador
                unos += 1
            contador +=1
        contador = 1
        if(unos==1):
            matriz[fila_uno][0][2]=1
            if(repetido==0):
                ecuacion_final.append(matriz[fila_uno][0])
                rellenar(matriz,fila_uno,columnas,i,filas)
                repetido+=1
            for s in range(len(ecuacion_final)):
                if(matriz[fila_uno][0] == ecuacion_final[s]):
                    repetido2 += 1
            if(repetido2==0 and repetido!=0):
                ecuacion_final.append(matriz[fila_uno][0])
                rellenar(matriz, fila_uno, columnas, i, filas)
                repetido+=1
            repetido2=0
        unos = 0
        i += 1
    ecuacion_final=analisis(matriz,ecuacion_final,columnas,filas)

    #ecuacion_final=contar(matriz,ecuacion_final,filas)
    #dibujar_matriz(matriz, columnas, filas)
    #print("--------------------------------------")
    #print(ecuacion_final)
    return ecuacion_final


if __name__ == "__main__":
    numero_entradas = int(input(
        "Introduce el numero de variables: ")) + 1  # En esta variable se guardaran el numero de variables o columnas
    filas = 2
    lista_minimos = []
    filas = filas ** (numero_entradas - 1)  # Las filas serán igual a 2 elevado al numero de entradas
    tablaverdad = crear_matriz([], numero_entradas, filas)  # Llamo la funcion que me crea la tabla de verdad

    tablaverdad = llenar_matriz(filas, numero_entradas, tablaverdad)  # se llena la matriz con los binarios

    matriz_nueva = minterms(tablaverdad, filas,
                            lista_minimos)  # se solicitan los valores decimales donde la funcion es valida y se extraen sus valores binarios corresondientes
    listMC = EMCclauskey(matriz_nueva, numero_entradas)

    matriz_nueva.clear()
    matriz_nueva = comparacionMC(listMC)
    print("---------------------------------------------")
    print("La ecuación sin verificar es: ")
    ecuacion(matriz_nueva)
    print(" ")
    matriz_final = llenar_verificacion(matriz_nueva, lista_minimos)  # minimos - columnas
    matriz_final = verificacion(matriz_final, len(lista_minimos) + 1, len(matriz_nueva) + 1)  # primero columnas

    print("---------------------------------------------------------------------")
    print("La ecuación verificada es: ")
    ecuacion(matriz_final)
