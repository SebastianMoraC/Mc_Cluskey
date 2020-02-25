import numpy as np

class nodo(object):

    def __init__(self,combinacion,binario):
        self.combinacion=combinacion
        self.binario=binario

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

if __name__ == "__main__":
    
    numero_entradas =int(input("Introduce el numero de variables: "))+2       #En esta variable se guardaran el numero de variables o columnas
    #Le sumo 2, porque en la primer columna, se almacenará el número en decimal desde [0-hasta el último bit] y la ultima contendra si la funcion es valida alli
    filas=2
    filas = filas**(numero_entradas-2)       #Las filas serán igual a 2 elevado al numero de entradas
    matriz = []     #definimos la matriz

    tablaverdad=crear_matriz(matriz,numero_entradas,filas)        #Llamo la funcion que me crea la tabla de verdad
    
    for i in range(filas):  #se llena la primer columna con los valores decimales
        tablaverdad[i][0]=i

    
    cantidad=filas/2 #cantidad correspondiente a cada grupo de "1" y "0" en cada fila ej:(para) en la primer fila van ocho unos y ocho ceros correspondiente
    repeticiones=1  #cantidad de veces que se tienen que repetir las cantidades anteriores

    for c in range(numero_entradas-2):  #recorre cada colunma
        for i in range(repeticiones):   #realiza la cantidad de repeticiones correspondientes a cada columna
            for a in range(cantidad):   #coloca la cantidad correspondiente de cada 0 por cada repeticion
                tablaverdad[a][c]=0
            for b in range(cantidad):
                tablaverdad[a][c]=0
        repeticiones=repeticiones*2
        cantidad=cantidad/2