def crear_matriz(n:int):
    matriz=[]
    for i in range (n):
        filas=[]
        for i in range (n):
            filas.append(0)
        matriz.append(filas)
    return matriz
matriz=crear_matriz(10)
matriz[7][4]=1
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




def walk_arriba(v,matriz):
    fila=posicion()[0]-v
    columna=posicion()[1]
    matriz[posicion()[0]][posicion()[1]]=0
    matriz[fila][columna]=1
    return matriz

def walk_abajo(v,matriz):
    fila=posicion()[0]+v
    columna=posicion()[1]
    matriz[posicion()[0]][posicion()[1]]=0
    matriz[fila][columna]=1
    return matriz
def walk_right(v,matriz):
    fila=posicion()[0]
    columna=posicion()[1]+v
    matriz[posicion()[0]][posicion()[1]]=0
    matriz[fila][columna]=1
    return matriz

def walk_left(v,matriz):
    fila=posicion()[0]
    columna=posicion()[1]-v
    matriz[posicion()[0]][posicion()[1]]=0
    matriz[fila][columna]=1
    return matriz






def walk(v:int,d:str):
    if d == 'front' or d == 'north':
        walk_arriba(v, matriz)
    elif d =='back' or d== 'south':
        walk_abajo(v, matriz)
    elif d =='right' or d== 'east':
        walk_right(v, matriz)
    elif d =='left' or d== 'west':
        walk_left(v, matriz)

    pass