def crear_matriz(n:int):
    matriz=[]
    for i in range (n):
        filas=[]
        for i in range (n):
            filas.append(0)
        matriz.append(filas)
    return matriz
matriz=crear_matriz(3)
for i in matriz:
    print (i)