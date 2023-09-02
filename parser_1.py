import tokenize as tk

with open('archivo.txt') as f:
    lineas = f.readlines()
tokenlist=[]
parrentesis=''

for i in lineas:
    if "(" in i:
        parrentesis+="("
    if ")" in i:
        parrentesis+=")"
    if "[" in i:
        parrentesis+="["
    if "]" in i:
        parrentesis+="]"
    if "{" in i:
        parrentesis+="{"
    if "}" in i:
        parrentesis+="}"

def isValid(token_list):
        parentesis = ["{", "}","[","]","(",")"]
        opcl = dict(('()', '[]', '{}'))
        stack = []
        for idx in token_list:
            if idx in parentesis:
                if idx in '([{':
                    stack.append(idx)
                elif len(stack) == 0 or idx != opcl[stack.pop()]:
                    return False
        return len(stack) == 0

if isValid(parrentesis):

    # Creates a tokenizer that transforms a txt file into a list. Each string of the of the txt file adopts
    # an index in the list.

    with tk.open(filename="archivo.txt") as file:
        tokens = tk.generate_tokens(file.readline)
        token_list = [token.string.lower() for token in tokens]

    tabulates = token_list.count("\t")
    blank_strings = token_list.count("")
    line_change = token_list.count("\n")
    for tabulate in range(0, tabulates): token_list.remove("\t")
    for blank_string in range(0, blank_strings): token_list.remove("")
    for line_change in range(0, line_change): token_list.remove("\n")


    # A list with all the structures used by the program that can´t be used as variables.
    reserved_structures = ["defvar","defproc","while","else","if","repeat","times", "jump", "walk","leap","turn","turnto","nop"]
    # Structures with similar behaviour.
    basics=["drop","get","grab","letgo"]
    # All commands used by the robot.
    primitives= ["drop","get","grab","letgo","jump","walk","leap","turn","turnto","nop"]
    # Control structures used in the program.
    control_structures = ["if", "while", "repeat", "times"]
    # Conditions that are used inside a loop.
    conditions = ["facing", "can", "not"]
    # Dicitionary that stores variables created by the user when invoking defProc.

    simple_commands = ["jump", "walk", "leap", "turn", "turnto", "drop", "get", "grab", "letgo", "nop"]
    conditionals = ["if", "else"]
    loop = ["while"]
    repeat_times = ["repeat", "times"]
    inside_var=[]
    comas=[',',"{", "}","[","]","(",")",";"]
    direcciones=['north','east','south','west']

    by_user = {}





    def def_var(i):
        """
        Describes the behaviour of a variable definition. 
        Variable definitions have the following form: 
        
        defVar nom 0 
        defVar x 0 
        defVar y 0

        Starts with the keyword defVar followed by a name fol-
        lowed by an initial value.
        """
        intern_counter = 0
        inside_var.append(token_list[i + 1])
        if not (token_list[i + 1].isalnum()):
            intern_counter += 1
        if not (token_list[i + 2].isnumeric()):
            intern_counter += 1
            
        return intern_counter


    def def_proc(i):
        """
        Describes the behaviour of a procedure definition.
        Procedure definitions have the following form:
        
        defProc putCB (c, b)
        {
            drop(c);
            letGo(b);
            walk(n)
        }
        
        defProc goNorth ()
        {
            while can (walk (1,north)) { walk (1,north)}
        }
        
        defProc goWest ()
        {
            if can (walk (1,west)) { walk (1,west)} else nop()
        }
        
        Starts with the keyword defProc followed by by a name,
        followed by a list of parameter in parenthesis separated by commas, followed
        by a block of commands.
        """
        intern_counter = 0
        comma_counter = 0
        
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
            
            """
            if closed[len(closed)-1] != "{":
                intern_counter += 1
            else:
                command_block(i)
            """
            
            closed.pop()
            closed.pop()

            if len (closed) == 0:
                by_user[token_list[i+1]] = 0
                return intern_counter, by_user
            
            else:
                by_user[token_list[i+1]] = []
                
                by_user_list = []
                
                if closed[0] == ",":
                    intern_counter += 1

                for z in range(len(closed)):
                    if z % 2 == 0:
                        by_user_list.append(closed[z])
                        
                        if not closed[z].isalnum():
                            intern_counter += 1
                    else:
                        if closed[z] == ",":
                            comma_counter += 1
                        if closed[z] != ',':
                            intern_counter += 1
                            
                if len(closed) % 2 == 0:
                    intern_counter += 1

        


        by_user.update({str(token_list[i+1]):by_user_list})
        for llave in by_user:
            inside_var.append(llave)
            for i in by_user[llave]:
                inside_var.append(i)
        
        
        
        return intern_counter, by_user

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

    def jumpcheck(i):
        intern_counter=0
        if token_list[i+1] != '(':
            intern_counter+=1
        if not(token_list[i+2].isnumeric()):
            intern_counter+=1
        if token_list[i+3] != ',':
            intern_counter+=1
        if not(token_list[i+4].isnumeric()):
            intern_counter+=1
        if token_list[i+5] != ')':
            intern_counter+=1 
        return intern_counter

    def walkcheck(i):
        direcciones=['front','right','left','back','north','east','south','west']
        intern_counter=0
        if token_list[i+1] != '(':
            intern_counter+=1
        if not(token_list[i+2].isnumeric()):
            if not(token_list[i+2] in inside_var):
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
            if token_list [i + 2] not in inside_var:
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

    counter = 0
    i = 0
    while i < len(token_list):
        
        if token_list[i] == "defvar":
            counter += def_var(i)
            i += 1
            
        if token_list[i] == "defproc":
            answers = def_proc(i)
            counter += answers[0]
            by_user = answers[1]
            i += 1
            
        if token_list[i] == "walk":
            counter += walkcheck(i)
            i += 1

        if token_list[i] == "jump":
            counter += jumpcheck(i)
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
            counter+= basiccomandscheck(i)
            i += 1
            
        else:
            i += 1

    


    i=0
    while i < len(token_list):

        if token_list[i] in reserved_structures: 
            pass
        elif token_list[i] in basics: 
            pass
        elif token_list[i] in primitives: 
            pass
        elif token_list[i] in control_structures: 
            pass
        elif token_list[i] in conditions:  
            pass
        elif token_list[i] in simple_commands: 
            pass
        elif token_list[i] in conditionals: 
            pass
        elif token_list[i] in loop:
            pass
        elif token_list[i] in repeat_times:  
            pass
        elif token_list[i] in inside_var:
            pass
        elif token_list[i] in comas:
            if token_list[i-1]==';': 
                counter+=1 
            if token_list[i] == "{":
                close = token_list[(i):len(token_list)]
                closed = []
            o = 0
            c = 0
            for value in close:
                closed.append(str(value))
                if value == "{":
                    o += 1
                elif value == "}":
                    c += 1
                    if o == c:
                        closed.append(close[close.index(value)])
                        break
        
        elif token_list[i] in by_user: 
            pass
        elif token_list[i].isnumeric():
            pass
        elif token_list[i] in by_user: 
            pass
        elif token_list[i] in direcciones: 
            pass

        elif token_list[i] == ' ':
            pass
        else:
            print(token_list[i], i)
            counter+=1
                
        i+=1
        
    if counter > 0:
        print("Invalid") 
    if counter == 0:
        print("Valid")
else:
    print("Invalid")