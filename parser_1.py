import tokenize as tk

with tk.open(filename="archivo.txt") as file:
    tokens = tk.generate_tokens(file.readline)
    token_list = [token.string.lower() for token in tokens]

tabulates = token_list.count("\t")
blank_strings = token_list.count("")
for tabulate in range(0, tabulates): token_list.remove("\t")
for blank_string in range(0, blank_strings): token_list.remove("")

reserved_structures = ["defvar", "defproc", "while", "else", "if", "repeat", "times"]


print(token_list)


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
    
    if token_list[i + 2] == "(":
        close = token_list[(i + 3):len(token_list)]
        closed = []
    
        for value in close:
            closed.append(str(value))
            if value == ")":
                closed.append(close[close.index(value) + 1])
                break
    
        if closed[len(closed)-1] != ";":
            intern_counter += 1
            closed.pop()
            closed.pop()
    
        closed.pop()
        closed.pop()
    
        #if closed[len(closed)-1] in [".", ","]:
            #intern_counter += 1

        if closed[0] == ",":
            intern_counter += 1
        
        for z in range(len(closed)):
            if z % 2 == 0:
                if not closed[z].isalnum():
                    intern_counter += 1
            else:
                if closed[z] != ',':
                    intern_counter += 1
                    
        if len(closed) % 2 == 0:
            intern_counter += 1

    return intern_counter

def def_proc2(i):
    intern_counter=0
    if not (token_list[i + 1].isalnum()):
        intern_counter += 1
    if token_list[i + 2] != "(":
        intern_counter += 1
    
    if token_list[i + 2] == "(":
        close = token_list[(i + 3):len(token_list)]
        closed = []
    
        for value in close:
            closed.append(str(value))
            if value == ")":
                closed.append(close[close.index(value) + 1])
                break
    
        if closed[len(closed)-1] != ";":
            intern_counter += 1
            closed.pop()
            closed.pop()
    
        closed.pop()
        closed.pop()
    
        #if closed[len(closed)-1] in [".", ","]:
            #intern_counter += 1

        if closed[0] == ",":
            intern_counter += 1
        
        for z in range(len(closed) - 1):
            if closed[z]==',':
                if not(closed[z-1].isalnum()):
                    intern_counter += 1
                if not(closed[z+1].isalnum()):
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
            i += 1
        if token_list[i] == "defproc":
            counter += def_proc(i)
            #counter += def_proc2(i)
            i += 1
    else:
        i += 1
    

print(counter)