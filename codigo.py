import tokenize as tk

with tk.open(filename="archivo.txt") as file:
    tokens = tk.generate_tokens(file.readline)
    token_list = [token.string.lower() for token in tokens]

tabulates = token_list.count("\t")
blank_strings = token_list.count("")
for tabulate in range(0, tabulates): token_list.remove("\t")
for blank_string in range(0, blank_strings): token_list.remove("")

reserved_structures = ["defvar","defproc","while","else","if","repeat","times","walk","leap","turn","turnto","nop"]
basics=["drop","get","grab","letgo"]
primitives= ["drop","get","grab","letgo","jump","walk","leap","turn","turnto","nop"]
control_structures = ["if", "while"]
conditions = ["facing", "can", "not"]
by_user = {}



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

print(4%2)



def isValid(token_list):
        '''
        Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
        An input string is valid if:
        Open brackets must be closed by the same type of brackets.
        Open brackets must be closed in the correct order.
        Every close bracket has a corresponding open bracket of the same type.
        USANDO PILAS
        SOLUCION COPIADA
    '''
        parentesis = ["{", "}","[","]","(",")"]
     # Create a pair of opening and closing parrenthesis...
        opcl = dict(('()', '[]', '{}'))
         # Create stack data structure...
        stack = []
        # Traverse each charater in input string...
        for idx in token_list:
            if idx in parentesis:
                # If open parentheses are present, append it to stack...
                if idx in '([{':
                    stack.append(idx)
                # If the character is closing parentheses, check that the same type 
                #opening parentheses is being pushed to the stack or not...
                # If not, we need to return false...
                elif len(stack) == 0 or idx != opcl[stack.pop()]:
                    return False
        # At last, we check if the stack is empty or not...
        # If the stack is empty it means every opened parenthesis is being closed 
        #and we can return true, otherwise we return false...
        return len(stack) == 0

print(isValid(token_list))
