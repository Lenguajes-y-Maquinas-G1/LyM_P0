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
    
    counter = 0 
    comas=[',',"{", "}","[","]","(",")",";"]
    i=0
    while i < len(token_list):
        if token_list[i] in comas:
            if token_list[i-1]==';': 
                counter+=1
            #TODOA MEJORAR 
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
    i += 1

print(counter)