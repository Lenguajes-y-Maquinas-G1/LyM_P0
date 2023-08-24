def crear_matriz(n:int):
    matriz=[]
    for i in range (n):
        filas=[]
        for i in range (n):
            filas.append(0)
        matriz.append(filas)
    return matriz
matriz=crear_matriz(3)
matriz[0][0]=1
for i in matriz:
    print (i)

def posicion():
    fila=0

    for fila in range (len(matriz)):
        if 1 in matriz[fila]:
            for valor in range(len(matriz[fila])):
                if matriz[fila][valor]==1:
                    return fila,valor
                    break


    pass

print(posicion())




def walk(v:int,d:str):
    pass