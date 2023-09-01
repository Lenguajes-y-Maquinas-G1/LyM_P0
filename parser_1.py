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
by_user = []


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
    
    by_user.append(token_list[i+1])
    
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

        if len (closed) == 0:
            return intern_counter
        else:

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


def turnto(i):
    direcciones=['north','east','south','west']
    intern_counter=0
    if token_list[i+1] != '(':
        intern_counter+=1
    if token_list[i+2] not in direcciones:
        intern_counter+=1
    if token_list[i+3] != ')':
        intern_counter+=1
        
    return intern_counter


def walkcheck(i):
    direcciones=['front','right','left','back','north','east','south','west']
    intern_counter=0
    if token_list[i+1] != '(':
        intern_counter+=1
    if not(token_list[i+2].isnumeric()):
        intern_counter+=1
    if token_list[i+3] != ',':
        intern_counter+=1
    if token_list [i + 4] not in direcciones:
        intern_counter+=1
    if token_list[i+5] != ')':
        intern_counter+=1
        
    return intern_counter


def leapcheck(i):
    direcciones=['front','right','left','back','north','east','south','west']
    intern_counter=0
    if token_list[i+1] != '(':
        intern_counter+=1
    if not(token_list[i+2].isnumeric()):
        intern_counter+=1
    if token_list[i+3]==")":
        pass
    if token_list[i+3]==",":
        if token_list [i + 4] not in direcciones:
            intern_counter+=1
        if token_list[i+5] != ')':
            intern_counter+=1
    if token_list[i+3] != ',' and token_list[i+3] != ')':
        intern_counter+=1
        
    return intern_counter


def turncheck(i):
    intern_counter=0
    direcciones=['left','right','around']
    if token_list[i+1] != '(':
        intern_counter+=1
    if token_list [i + 2] not in direcciones:
        intern_counter+=1
    if token_list[i+3] != ')':
        intern_counter+=1
        
    return intern_counter


def basiccomandscheck(i):
    intern_counter=0
    if token_list[i+1] != '(':
        intern_counter+=1
    if not(token_list [i + 2].isnumeric()):
        intern_counter+=1
    if token_list[i+3] != ')':
        intern_counter+=1
        
    return intern_counter


def nop(i):
    intern_counter=0
    if token_list[i+1] != '(':
        intern_counter+=1
    if token_list[i+2] != ")":
        intern_counter+=1
        
    return intern_counter


def can(i):
    intern_counter=0
    if token_list[i+1] != '(':
        intern_counter+=1
    if token_list[i+2] not in primitives:
        intern_counter+=1
        
    return intern_counter


def conditional(i):
    intern_counter = 0
    if token_list[i+1] != "if":
        intern_counter += 1
    if token_list[i+2] != "can":
        intern_counter += 1
    if token_list[i+3] != "(":
        intern_counter += 1
    else:
        if token_list[i+4] in primitives:
            pass #TODO: Terminar función.
    
    return intern_counter


def command_block(i):
    intern_counter = 0
    
    while i < len(token_list):
        if token_list[i + 1] in primitives:
            pass
            
    return intern_counter 
            
    

counter = 0
i = 0
while i < len(token_list):
    if token_list[i] in reserved_structures:
        if token_list[i] == "defvar":
            counter += def_var(i)
            i += 1
        if token_list[i] == "defproc":
            counter += def_proc(i)
            i += 2
        if token_list[i] == "{":
            counter += command_block(i)
            i += 1
        if token_list[i] == "walk":
            counter += walkcheck(i)
            i += 1
        if token_list[i] == "leap":
            counter += leapcheck(i)
            i += 1
        if token_list[i] == "turn":
            counter += turncheck(i)
            i += 1
        if token_list[i] == "turnto":
            counter += turnto(i)
            i += 1
        if token_list[i] == "nop":
            counter += nop(i)
            i += 1
    if token_list[i] in basics:
        print('aaaa')
        counter+= basiccomandscheck(i)
        i += 1
    else:
        i += 1
    

if counter >0:
    print("NO")
if counter==0:
    print("SI")