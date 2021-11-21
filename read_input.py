def ignore_indent(string):
    new_string = ""
    start_char = False
    for c in string:
        if (c == ' ' and not start_char):
            continue
        elif (c!= ' ' and not start_char):
            start_char = True
            new_string += c
        elif (start_char):
            new_string += c
    return new_string

reserved_words = ["if"]
mandatory_sym = [":"]
operators = ["+", "-", "/", "*", ">", ">=", "<", "<=", "==", "!=", "!"]
EMPTY_STRING = ""
VAR_STRING = "/var/"
f = open('test.py', 'r')
data = f.read()
processed_data = []
temp = data
for key in (reserved_words + mandatory_sym):
    temp = temp.replace(key, EMPTY_STRING)

variables_with_operators = temp.split("\n")
#disini idenya adalah merubah operasi operator dari :
# a > b (contoh), menjadi
# /var/ > /var/, untuk kemudahan pemrosesan CFG. masih in progress
"""
for var in variables:
    data = data.replace(ignore_indent(var), VAR_STRING)

data = data.split("\n")
for i in range(len(data)):
    data[i] = ignore_indent(data[i])
    data[i] += '\n'

print(data)
input()
"""

