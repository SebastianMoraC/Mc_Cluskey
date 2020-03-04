def crear_matriz(matriz, columnas, filas):  # Funcion que crea matrices
    for i in range(filas):
        matriz.append([])
        for j in range(columnas):
            if j == 0:
                matriz[i].append(i)
            else:
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


def minterms(matriz, filas):
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
                iteracion += 1
            else:
                break
        else:
            print("INGRESE UN NUMERO ENTRE: [0-", filas - 1, "]")

    return matriz_nueva


def EMCclauskey(matriz, variables, filas):  # se ordenan los valores binarios por cantidad de unos presentes
    Mcclauskey = list()  # lista final donde estara la agrupacion por unos
    tempcombinaciones = list()  # lista temporal donde se almacenara cada grupo de unos
    tempcombinacion = list()
    tempdecimal = list()  # lista para los valores decimales Nota: en primera instancia sera un unico valor pereo mientras se ejecuta el rpoceso de mclauskey se obtendran mas valores

    iteracion = 0
    while iteracion <= variables:
        for a in range(filas):
            count = 0
            for b in range(1, variables):
                if matriz[a][b] == 1:
                    count += 1
                tempcombinacion.append(matriz[a][b])
                # como #"$"!#"$!#!$ se borra toda una fila de la matriz?"
            if count == iteracion:
                tempdecimal.append(matriz[a][0])
                n = nodo(tempcombinacion, tempdecimal)
                tempcombinacion.clear()
                tempdecimal.clear()
                tempcombinaciones.append(n)
        Mcclauskey.append(tempcombinaciones)
        tempcombinaciones.clear()
        iteracion += 1

    return Mcclauskey


def comparacionMC1(MCclauskey):
    Mcclauskeycomplete = list()  # lista que contendra las agrupaciones de las combinaciones resultantes
    tempcombinaciones = list()  # lista que tendra temporalmente cada agrupacion

    templist1 = list()  # lista para tomar una agrupacion
    templist2 = list()  # lista para tomar la siguiente agrupacion

    i = 0
    while len(MCclauskey) >= i + 1:  # comenzamos a sacar cada agrupacion de 1
        templist1 = MCclauskey[i]  # tomamos una agrupacion de unos
        templist2 = MCclauskey[i + 1]  # y luego tomamos la siguiente agrupacion

        for a in templist1:  # e comienza a recorrer la primera agrupacion con le fin de sacar una elemento y compararlos con todos los de la agrupacion siguiente
            for b in templist2:  # se recorre la segunda agrupacion para compararla completamente con el elemento de sacado anteiormente
                if ((a.combinacion.count(1) + 1 > b.combinacion.count(1)) or (
                        a.combinacion.count(1) < b.combinacion.count(
                        1))):  # se consulta si estos dos elemetos tienen un bit de diferencia
                    tempbinary = list()  # esta variable temporal se encargara de solamente guardar el binario
                    tempdecimal = list()
                    for c in range(len(
                            a.combinacion)):  # se comienzan a recorrer ambos elementos con el fin de encontrar la posicion donde se encuentra el uno en comun
                        if a.combinacion[c] != b.combinacion[
                            c]:  # se consulta si precisamente la posisicon en cuestion contiene el cambio de bit
                            tempbinary.append("-")  # se registra el cambio de bit
                        else:
                            tempbinary.append(a.combinacion[c])  # si no se guarda la posicion normal
                    tempdecimal.append(a.decimal)  # se guarda el decimal del primer inplicante
                    tempdecimal.append(b.decimal)  # se guarda el decimal del segundo inplicante
                    ni = nodo(tempbinary,
                              tempdecimal)  # se crea el objeto que guarda ambos datos tanto binarios como decimales
                    tempbinary.clear()  # se vacia con el fin de evitar redundancia
                    tempdecimal.clear()
                    tempcombinaciones.append(ni)  # se guarda en la agripacion correspondiente
        Mcclauskeycomplete.append(tempcombinaciones)  # se guarda las agrupaciones y se procede a al siguiente grupo


if __name__ == "__main__":
    numero_entradas = int(input(
        "Introduce el numero de variables: ")) + 2  # En esta variable se guardaran el numero de variables o columnas
    # Le sumo 2, porque en la primer columna, se almacenará el número en decimal desde [0-hasta el último bit] y la ultima contendra si la funcion es valida alli
    filas = 2 ** (numero_entradas - 2)  # Las filas serán igual a 2 elevado al numero de entradas
    tablaverdad = crear_matriz([], numero_entradas, filas)  # Llamo la funcion que me crea la tabla de verdad
    tablaverdad = llenar_matriz(filas, numero_entradas, tablaverdad)

    print(
        "--------------------------------------------------------------------------------------------------------------------")
    dibujar_matriz(tablaverdad, numero_entradas, filas)
    matriz_nueva = minterms(tablaverdad, filas)

    print(
        "--------------------------------------------------------------------------------------------------------------------")
    print("Los minterms son: ", matriz_nueva)
    #listMC = EMCclauskey(tablaverdad, numero_entradas - 1, filas)  # primera agrupacion del maclauske
