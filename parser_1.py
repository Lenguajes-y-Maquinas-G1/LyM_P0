import tokenize as tk

with tk.open(filename="archivo.txt") as file:
    tokens = tk.generate_tokens(file.readline)
    token_list = [token.string.lower() for token in tokens]

tabulates = token_list.count("\t")
blank_strings = token_list.count("")
for tabulate in range(0, tabulates): token_list.remove("\t")
for blank_string in range(0, blank_strings): token_list.remove("")

reserved_structures = ["defvar", "defproc", "while", "else", "if", "repeat", "times"]

def check_code():