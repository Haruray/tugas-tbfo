reserved_words = ["if"]
mandatory_sym = [":"]
operators = ["+", "-", "/", "*", ">=", ">", "<=", "<", "==", "!=", "!"]
EMPTY_STRING = ""
VAR_STRING = "/var/"

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
def ignore_indent_before_after(string):
    new_string = ignore_indent(string)
    new_string = ignore_indent(new_string[::-1])
    return new_string[::-1]
def ignore_indent_array(array):
    new_array = []
    for e in array:
        new_array.append(ignore_indent_before_after(e))
    return new_array

def operator_split(string_array):
    global operators
    result = []
    for string in string_array:
        temp = [string]
        i = 0
        while (len(temp)==1):
            temp = string.split(operators[i])
            i += 1
        result += temp
    result = ignore_indent_array(result)
    result = list(set(result))
    return result

def process_input():
    global reserved_words, mandatory_sym, operators,EMPTY_STRING,VAR_STRING
    f = open('test.py', 'r')
    data = f.read()
    processed_data = []
    temp = data
    for key in (reserved_words + mandatory_sym):
        temp = temp.replace(key, EMPTY_STRING)

    variables_with_operators = ignore_indent_array(temp.split("\n"))
    variables = operator_split(variables_with_operators)
    variables_with_operators_processed = []

    for var_op in variables_with_operators:
        temp_var_op = var_op
        for var in variables:
            temp_var_op = temp_var_op.replace(var, VAR_STRING)
        variables_with_operators_processed.append(temp_var_op)
    print(variables_with_operators_processed)
        
    #disini idenya adalah merubah operasi operator dari :
    # a > b (contoh), menjadi
    # /var/ > /var/, untuk kemudahan pemrosesan CFG. masih in progress

    for i in range(len(variables_with_operators)):
        data = data.replace(variables_with_operators[i], variables_with_operators_processed[i])

    data = data.split("\n")
    for i in range(len(data)):
        data[i] = ignore_indent(data[i])
        data[i] += '\n'
        
    return data

process_input()


