
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

def EMCclauskey(matriz,variables): # se ordenan los valores binarios por cantidad de unos presentes
    Mcclauskey=list() #lista final donde estara la agrupacion por unos
    tempcombinaciones=list() #lista temporal donde se almacenara cada grupo de unos 
    tempcombinacion=list()
    tempdecimal=list() #lista para los valores decimales Nota: en primera instancia sera un unico valor pereo mientras se ejecuta el rpoceso de mclauskey se obtendran mas valores
    n1=list()

    iteracion=0 #se itera la cantidad de variables que hay iniciando desde 0
    flag=0 # una bandera para saber si existen agrupaciones de unos adecuadas para guardas
    while iteracion <= variables: # se utilizara como control para que se guarden los valores por cantidad de unos  
        for a in range(len(matriz)): #se reorre primero por cada fila
            flag=0
            count=0 # contador de unos
            t=range(1,variables) # por cuestiones de funcionamiento es necesario esta asignacion
            for b in t:# recorre por columnas, se empieza desde la posicion 1 por el hehcho de que en la primera posicion esta  el numero representado en decimal
                if matriz[a][b] == 1: # condicional para contar
                    count+=1
                tempcombinacion.append(matriz[a][b]) # se guarda la combinacion binaria
                # como #"$"!#"$!#!$ se borra toda una fila de la matriz?"
            if count == iteracion: # se verifica si la cantidad de unso coincide con la cantidad que se esta trabajando actualmente
                flag=1
                tempdecimal.append(matriz[a][0]) # se guarda el decimal
                n1.append(tempcombinacion)
                n1.append(tempdecimal)
                n1.append(0)
                tempcombinaciones.append(n1) # finalmente se guarda la combinacion de binarios en una lista
                
            n1=[]
            tempcombinacion=[] # se vacia la lista para evitar ambiguedad
            tempdecimal=[]
            
        if tempcombinaciones != []:
            Mcclauskey.append(tempcombinaciones) # finalmente se guarda la lista de binarios en una lista

        tempcombinaciones=[]
        iteracion+=1 # aumenta la iteraion con el fin de comprobar todas las cantidades de unos
    return Mcclauskey

def ecuacion(Matriz, implicantes):
    tempecuacion=list() #lista que contendra la ecuacion de la tupla y los valores decimales que lo formaron
    temp=list() # lista para agrupar en una sola lista los caracteres y los numero
    tempcaracter=list() #lista para guardar los caracteres
    tempnumber=list() # lista para guardar los decimales
    strin=""# variable para guardar el texto correspondiente a 
    Leters=["A","B","C","D","E","F","G","H","I","J","K","L","M","N"] # letras para representar las variables
    stemp1=""
    ubicacion=0
    for a in Matriz: # se recorre la lista
        for b in a: # se recorre las listas contenidas
            flag=0
            if b == a[-1]: # en caso de que se trate el ultimo elemento no se colocara un "+" al final
                count=0# variable para recorrer la lista de letras
                for c in b[0]:# se recorre el binario
                    if c == 0: # se averigua si es 0
                        strin=strin+"not("+Leters[count]+")"# se guardan los caranteres
                        print("not("+Leters[count]+")",end="")# se muestran los caracteres
                    elif c == 1: # para el caso de que sea 1
                        strin=strin+Leters[count]
                        print(Leters[count],end="")
                    count+=1
                flag+=1
            else: # en caso contrario se imprimiran los caracteres y un "+" al final
                count=0
                for c in b[0]:
                    if c == 0:
                        strin=strin+"not("+Leters[count]+")"
                        print("not("+Leters[count]+")",end="")
                    elif c == 1:
                        strin=strin+Leters[count]
                        print(Leters[count],end="")
                    count+=1
                flag+=1
                print(" + ",end="")

            if flag == 1:
                stemp1=strin
                tempcaracter.append(strin) # finalmente se guarda la cadena con la ecuacion correspondiente al binario resultante
                for i in b[1]: # se almacena los valores decimales que formaron el binario resultante
                    tempnumber.append(i)
                temp.append(tempcaracter) # se guardan los caracteres en una lista junto con los decimales
                temp.append(tempnumber)
                tempecuacion.append(temp) # se guarda la lista que contiene tanto la ecuacion como los decimales
                ubicacion=len(tempecuacion)-1
            else:
                if stemp1 != strin:
                    stemp1 = strin

                    #######################################
                    tempcaracter.append(strin) # finalmente se guarda la cadena con la ecuacion correspondiente al binario resultante
                    for i in b[1]: # se almacena los valores decimales que formaron el binario resultante
                        tempnumber.append(i)
                    temp.append(tempcaracter) # se guardan los caracteres en una lista junto con los decimales
                    temp.append(tempnumber)
                    tempecuacion.append(temp) # se guarda la lista que contiene tanto la ecuacion como los decimales
                    ubicacion=len(tempecuacion)-1
                elif stemp1 == strin:
                    print("entro")
                    for i in b[1]: # se almacena los valores decimales que formaron el binario resultante
                        (tempecuacion[ubicacion])[1].append(i)

            strin="" # se vacia para evitar concurrencia
            tempcaracter=[]
            tempnumber=[]

    # en caso de que hayan aparecido primeros implicantes se revisa la lista si existe alguno y se realiza de nuevo el anterior proceso
    if len(implicantes) > 0:
        print(" + ",end="")             
        for a in implicantes:
            if a == implicantes[-1]:
                count=0
                for c in a[0]:
                    if c == 0:
                        strin=strin+"not("+Leters[count]+")"
                        print("not("+Leters[count]+")",end="")
                    elif c == 1:
                        strin=strin+Leters[count]
                        print(Leters[count],end="")
                    count+=1
            else:
                count=0
                for c in a[0]:
                    if c == 0:
                        strin=strin+"not("+Leters[count]+")"
                        print("not("+Leters[count]+")",end="")
                    elif c == 1:
                        strin=strin+Leters[count]
                        print(Leters[count],end="")
                    count+=1
                print(" + ",end="")
            tempcaracter.append(strin) # finalmente se guarda la cadena con la ecuacion correspondiente al binario resultante
            strin="" # se vacia para evitar concurrencia
            for i in a[1]: # se almacena los valores decimales que formaron el binario resultante
                tempnumber.append(i)
            temp.append(tempcaracter) # se guardan los caracteres en una lista junto con los decimales
            temp.append(tempnumber)
            tempcaracter=[]
            tempnumber=[]
            tempecuacion.append(temp) # se guarda la lista que contiene tanto la ecuacion como los decimales

    return tempecuacion

def revision(a,b): # se confirma se exactamente cambia un bit entre los dos binarios en cuestion
    counte=0

    for i in range(len(a)): # se va a recorrer de extremo a extremo cada binario
        if not(a[i] == b[i]): # se consulta si hay presente un cambio entre los dos bits en cuestion
            counte+=1# en caso tal se cuenta la cantidad de cambios
    if counte == 1:
        return True#si solo existe un cambio de un solo bit se podra proceder a la mezcla
    else:
        return False # en caso contraio no se podra ejecutar la mezcla

def comparacionMC(MCclauskey):
    Mcclauskeycomplete=list() #matriz que contendra las agrupaciones de las combinaciones resultantes
    tempMcclauskeycomplete=list()
    tempcombinaciones=list() #lista que tendra temporalmente cada agrupacion
    implicantes=list() # se guardaran todas las combinaciones binarias que no se mexclaron en algun punto o 
    
    templist1=list() #lista para tomar una agrupacion 
    templist2=list() #lista para tomar la siguiente agrupacion
    ni=list() #lista de decimal combiancion binaria y validacion

    fin=0
    while fin != 1:
        i=0
        while len(MCclauskey) > i+1: # comenzamos a sacar cada agrupacion de 1
            templist1=MCclauskey[i] # tomamos una agrupacion de unos
            templist2=MCclauskey[i+1] #y luego tomamos la siguiente agrupacion
            
            
            for a in templist1: #e comienza a recorrer la primera agrupacion con le fin de sacar una elemento y compararlos con todos los de la agrupacion siguiente
                for b in templist2: # se recorre la segunda agrupacion para compararla completamente con el elemento de sacado anteiormente
                    if ((
                        (a[0].count(1)+1 == b[0].count(1)) or 
                        (a[0].count(1) == b[0].count(1)+1) or
                        ( (a[0].count(1)+1 == b[0].count(1))  and (a[0].count('-') == b[0].count('-'))) or
                        ( (a[0].count(1) == b[0].count(1)) and (a[0].count('-')+1 == b[0].count('-'))) or
                        ( (a[0].count(1) == b[0].count(1)+1)  and (a[0].count('-') == b[0].count('-'))) or
                        ( (a[0].count(1) == b[0].count(1)) and (a[0].count('-') == b[0].count('-')+1))
                        ) and revision(a[0],b[0] ) == True
                        ):# se consulta si estos dos elemetos tienen un bit de diferencia
                        tempbinary= list() # esta variable temporal se encargara de solamente guardar el binario
                        tempdecimal=list()
                        for c in range(len(a[0])): # se comienzan a recorrer ambos elementos con el fin de encontrar la posicion donde se encuentra el uno en comun
                            if (a[0])[c] != (b[0])[c]: # se consulta si precisamente la posisicon en cuestion contiene el cambio de bit
                                tempbinary.append('-') # se registra el cambio de bit
                            else:
                                tempbinary.append((a[0])[c])# si no se guarda la posicion normal
                        for d in range(len(a[1])): # se guarda el decimal del primer inplicante
                            tempdecimal.append((a[1])[d])
                        for d in range(len(b[1])): # se guarda el decimal del segundo inplicante
                            tempdecimal.append((b[1])[d])         

                        ni.append(tempbinary)
                        ni.append(tempdecimal)
                        ni.append(0) # en las 3 anteriores lineas se crea la tupla que contiene la lista de decimales que formaron el binario en cuestion y un int de validacion para saber si se mexcla o no
                        tempbinary=[] # se vacia con el fin de evitar redundancia
                        tempdecimal=[]
                        tempcombinaciones.append(ni)# se guarda en la agripacion correspondiente
                        ni=[] 
                        b[2]=1 # se cambia la posicion de la validacion para saber que fue mezclado
                        a[2]=1
            if tempcombinaciones != []:   
                tempMcclauskeycomplete.append(tempcombinaciones)# se guarda las agrupaciones y se procede a los siguiente grupo
            tempcombinaciones=[]
            i+=1
        comprobaciondefin=0 # se utilizara para saber si se mezclo algun elemento
        
        if len(tempMcclauskeycomplete) == 0:
            break

        for a in MCclauskey: # se recorre cada lista
            for b in a: # se recorres cada binario
                if b[2] == 0: # en caso tal de que la validacion de mezcla sea 0
                    implicantes.append(b) #dicho elelemtno pasa a ser un implicante
                    comprobaciondefin+=1 # se cuenta cuantos elementos no fueron mezclados
        
        elementos=0
        for a in MCclauskey: # se cuenta el total de binarios en la matriz
            elementos+=len(a)

        if (len(MCclauskey) == 1) or (elementos == comprobaciondefin): #en caso tal de que solo haya una sola lista o ninguno de los elementos de la lista se haya podido mezclar se finaliza 
            fin=1
            break
        
        MCclauskey=[]
        for a in tempMcclauskeycomplete:
            MCclauskey.append(a)

        Mcclauskeycomplete.append(tempMcclauskeycomplete)
        tempMcclauskeycomplete=[]
    ec=list()
    ec=ecuacion(Mcclauskeycomplete[-1],implicantes)    

    return Mcclauskeycomplete

if __name__ == "__main__":
    
    numero_entradas =int(input("Introduce el numero de variables: "))+1       #En esta variable se guardaran el numero de variables o columnas
    filas=2
    filas = filas**(numero_entradas-1)       #Las filas serán igual a 2 elevado al numero de entradas

    tablaverdad=crear_matriz([],numero_entradas,filas)        #Llamo la funcion que me crea la tabla de verdad
    
    tablaverdad=llenar_matriz(filas, numero_entradas, tablaverdad) #se llena la matriz con los binarios 

    matriz_nueva=minterms(tablaverdad,filas) # se solicitan los valores decimales donde la funcion es valida y se extraen sus valores binarios corresondientes
    
    listMC=EMCclauskey(matriz_nueva,numero_entradas)

    matriz_nueva.clear()
    matriz_nueva=comparacionMC(listMC)

