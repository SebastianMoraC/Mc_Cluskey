def crear_matriz(matriz, columnas, filas):  # Funcion que crea matrices
    for i in range(filas):
        matriz.append([])
        for j in range(columnas):
            if j==0:
                matriz[i].append(i)
            else: matriz[i].append(0)
    return matriz
def dibujar_matriz(matriz, columnas, filas):  # Funcion que dibuja matrices
    for i in range(filas):
        for j in range(columnas):
            print(matriz[i][j], end="")  # El end se utiliza para que no se haga cambio de linea al imprimir en pantalla
        print("")  # Con esta linea hago el cambio de columna


def llenar_matriz(filas, columnas, matriz):  #Esta funcion llena las matrices de ceros y unos
    cantidad=filas//2
    repeticiones = 1
    iteracion= 0

    for c in range(1,columnas):  # recorre cada columna
        for i in range(repeticiones):  # realiza la cantidad de repeticiones correspondientes a cada columna

            for a in range(cantidad):  # coloca la cantidad correspondiente de cada 0 por cada repeticion
                matriz[iteracion][c] = 0
                iteracion=iteracion+1  #La iteraccion me indica que fila irá el numero
            for b in range(cantidad):  # coloca la cantidad correspondiente de cada 1 por cada repeticion
                matriz[iteracion][c] = 1
                iteracion = iteracion + 1
        repeticiones = repeticiones * 2  # aumenta la cantidad de repeticiones en cada fila
        cantidad = cantidad // 2  # Divide la cantidad de 0 y 1 que entraran
        iteracion=0
    return matriz

def minterms(matriz,filas):
    matriz_nueva=[]
    iteracion=0
    print("--------------------------------------------------------------------------------------------------------------------")
    print("Ingrese el numero -1 cuando quiera finalizar de ingresar numeros, los numeros deben estar entre: [0-", filas-1,"]")
    #for i in range(filas):
    while iteracion<filas:
        valor=int(input("Ingrese el minterm: "))
        if valor<=filas-1:
            if valor!=-1:
                matriz_nueva.append(matriz[valor])
                iteracion += 1
            else:
                break
        else:
            print("INGRESE UN NUMERO ENTRE: [0-",filas-1,"]")


    return matriz_nueva
if __name__ == "__main__":

    numero_entradas = int(input("Introduce el numero de variables: ")) +1  # En esta variable se guardaran el numero de variables o columnas
    # Le sumo 2, porque en la primer columna, se almacenará el número en decimal desde [0-hasta el último bit] y la ultima contendra si la funcion es valida alli
    filas = 2 ** (numero_entradas - 1)  # Las filas serán igual a 2 elevado al numero de entradas
    tablaverdad = crear_matriz([], numero_entradas, filas)  # Llamo la funcion que me crea la tabla de verdad
    tablaverdad=llenar_matriz(filas, numero_entradas, tablaverdad)

    print("--------------------------------------------------------------------------------------------------------------------")
    dibujar_matriz(tablaverdad,numero_entradas,filas)
    matriz_nueva=minterms(tablaverdad,filas)

    print("--------------------------------------------------------------------------------------------------------------------")
    print ("Los minterms son: ",matriz_nueva)
