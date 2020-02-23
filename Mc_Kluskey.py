
numero_entradas =int(input("Introduce el numero de variables: "))+1       #En esta variable se guardaran el numero de variables o columnas
#Le sumo 1, porque en la primer columna, se almacenará el número en decimal desde [0-hasta el último bit]
filas=2
filas = filas**(numero_entradas-1)       #Las columnas será igual a 2 elevado al numero de entradas
matriz = []     #definimos la matriz


def crear_matriz(matriz,columnas,filas):        #Funcion que crea matrices
    for i in range(filas):
        matriz.append([])
        for j in range(columnas):
            matriz[i].append(0)
    return matriz


def dibujar_matriz(matriz,columnas,filas):      #Funcion que dibuja matrices
    for i in range(filas):
        for j in range(columnas):
            print(matriz[i][j],end="")              #El end se utiliza para que no se haga cambio de linea al imprimir en pantalla
        print("")                       #Con esta linea hago el cambio de columna
#def llenar_matriz():          #Cree acá la función que llene la matriz

matriz=crear_matriz(matriz,numero_entradas,filas)        #Llamo la funcion que me crea la matriz
dibujar_matriz(matriz,numero_entradas,filas)                #Llamo funcion que me dibuja la matriz
