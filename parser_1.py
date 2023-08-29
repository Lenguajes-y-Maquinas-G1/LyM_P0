import tokenize as tk

with tk.open(filename="archivo.txt") as file:
    tokens = tk.generate_tokens(file.readline)
    token_list = [token.string.lower() for token in tokens]

tabulates = token_list.count("\t")
blank_strings = token_list.count("")
for tabulate in range(0, tabulates): token_list.remove("\t")
for blank_string in range(0, blank_strings): token_list.remove("")

reserved_structures = ["defvar", "defproc", "while", "else", "if", "repeat", "times"]

def def_var(i):
    intern_counter = 0
    if not (token_list[i + 1].isalnum()):
        intern_counter += 1
    if not (token_list[i + 2].isnumeric()):
        intern_counter += 1
        
    return intern_counter


def def_proc(i):
    intern_counter = 0
    if not (token_list[i + 1].isalnum()):
        intern_counter += 1
    if token_list[i + 2] != "(":
        intern_counter += 1
        
    close = token_list[(i + 3):len(token_list)]
    closed = token_list[(i + 3):close]
    
    if closed[len(closed)-1] in [".", ","]:
        intern_counter += 1
    
    for value in range(len(closed)):
        if not(closed[value].isalnum()) or not(closed[value] == ","):
            intern_counter += 1 
        if closed[value] == ",":
            if not (closed[value - 1].isalnum()):
                intern_counter += 1
            if not (closed[value + 1].isalnum()):
                intern_counter += 1

    return intern_counter

        
def command_block():
    pass

counter = 0
i = 0
while i < len(token_list):
    if token_list[i] in reserved_structures:
        if token_list[i] == "defvar":
            counter += def_var(i)
        if token_list[i] == "defproc":
            counter += def_proc(i)

"""
def def_var(counter):
    if token_list[counter + 1] != "":
        pass
    else:
        return False
    
    if token_list[counter + 2].isnumeric:
        pass
    else:
        return False




def prueba(token_list):
    i=0
    while i < len(token_list):
        def_var(i)
        i+=1
    return True

def prueba2(token_list):
    i=0
    while i < len(token_list):
        if token_list[i]=="defvar":
            if token_list[i + 1] in  reserved_structures or token_list[i + 1]=='\n' :
                return False
            
            if not(token_list[i+ 2].isnumeric()):
                return False
        i+=1
    return True

print(prueba2(token_list))

#print(token_list)
    
"""  