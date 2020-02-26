

class nodo(object): #objeto para armacenar tupla de binario y bumero decimal

    def __init__(self,combinacion,binario):
        self.combinacion=combinacion
        self.decimal=decimal

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

def llenar_matriz(filas,numero_entradas,matriz):          #Cree acá la función que llene la matriz
    cantidad=filas/2 #cantidad correspondiente a cada grupo de "1" y "0" en cada fila ej:(para) en la primer fila van ocho unos y ocho ceros correspondiente
    repeticiones=1  #cantidad de veces que se tienen que repetir las cantidades anteriores

    for c in range(numero_entradas-2):  #recorre cada colunma
        for i in range(filas):  #se llena la primer columna con los valores decimales
            tablaverdad[i][0]=i
        for i in range(repeticiones):   #realiza la cantidad de repeticiones correspondientes a cada columna
            for a in range(cantidad):   #coloca la cantidad correspondiente de cada 0 por cada repeticion
                tablaverdad[a][c]=0
            for b in range(cantidad):    #coloca la cantidad correspondiente de cada 0 por cada repeticion
                tablaverdad[a][c]=0
        repeticiones=repeticiones*2  #aumenta la cantidad de repeticiones en cada fila
        cantidad=cantidad/2            #cantidad de 1 y 0 a ingresar a la tabla

def comparacionesMC(Mcclaukey1):
    Mcclaukeycomplete=list()
    templist1=list()
    templist2=list()

    for i in Mcclaukey1:
        ###################################################


if __name__ == "__main__":
    
    numero_entradas =int(input("Introduce el numero de variables: "))+2       #En esta variable se guardaran el numero de variables o columnas
    #Le sumo 2, porque en la primer columna, se almacenará el número en decimal desde [0-hasta el último bit] y la ultima contendra si la funcion es valida alli
    filas=2
    filas = filas**(numero_entradas-2)       #Las filas serán igual a 2 elevado al numero de entradas
    
    tablaverdad=crear_matriz([],numero_entradas,filas)        #Llamo la funcion que me crea la tabla de verdad
    
    llenar_matriz(filas,numero_entradas,tablaverdad)

    Mcclaukey1=list() #lista de todas las grupaciones
    listac=list() #lista para grupar por cantidad de 1
    templist=list() #lista para recolectar el binario
    
    iterador=1
    while iterador <= numero_entradas-2:  # se itera la cantidad de veces como variables hayan
        for i in range(filas):    #se busca en cada fila
            if tablaverdad[i][numero_entradas-1] == 1: # se verifica si la funcion es valida en ese numero
                count=0
                for a in range(numero_entradas-1): #se extrae el numero binario
                    templist.append(tablaverdad[i][a]) #se guarda en la lista
                    if tablaverdad[i][a] == 1: # se cuenta la cantidad de unos que contiene la tupla bianria
                            count+=1 #contador de unos
                if count == iterador: #en caso de que cuente con la cantidad de unos correspondientes al iterador={1,2,3,..,n}
                    n1=nodo(templist,tablaverdad[i][0]) #se añade al nodo
                    listac.append(n1) #finalmente se agrea a la lista correspondiente a esta cantidad de 1
        Mcclaukey1.append(listac) #se añade la lista de tuplas ordenada segun su cantidad de unos
        iterador+=1 # aumenta iterador para buscar la siguiente cantidad de unos
    
