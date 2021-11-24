import re
import copy
from finite_automata import *

reserved_words = {
    "if" : "a", 
    "class" : "b", 
    "False" : "c", 
    "True" : "d", 
    "is" : "e",
    "return" : "f",
    "None" : "g",
    "continue" :"h",
    "for" : "i",
    "def" : "j",
    "from" : "k",
    "while" : "n",
    "with" : "m",
    "as" : "o",
    "elif" : "p",
    "else" : "q",
    "import" : "r",
    "pass" : "s",
    "break" : "t",
    "in" : "u",
    "raise" : "v",
    "range" : "w",
    }
mandatory_sym = [":", ",", "(", ")", "[", "]", ".", "{", "}"]
operators = ["+", "-", "/", "*", ">", ">=", "<=", "<", "==", "!=", "and","or", "not", "+=", "-=", "%","="]
operators_substitute = {
    "and" : "&",
    "or" : "#",
    "not" : "!"
}
EMPTY_STRING = ""
VAR_STRING = "^"
CONTS_STRING = "~"
NEWLINE_CONST = "@"

VARIABLES = []

def variable_or_const_check(string):
    """
    CEK APAKAH STRING MERUPAKAN VARIABLE ATAU CONST
    CONST DISINI ADALAH APAPUN YG TIDAK BISA MENJADI ANGKA, DAN STRING TERMASUK CONST JUGA
    """
    is_const = False
    if ((string[0]=="\"" or string[0]=="\'") and (string[len(string)-1]=="\"" or string[len(string)-1]=="\'")):
        is_const = True
        return is_const
    else:
        try:
            number = int(string)
            number = float(string)
            is_const = True
        except:
            is_const = False
        finally:
            return is_const

def process_input(filename):
    global reserved_words, mandatory_sym, operators,EMPTY_STRING,VAR_STRING, VARIABLES
    f = open(filename, 'r')
    #data = f.read()
    data = ""
    comment_flag = False
    #LANGKAH 0 ; PER BARIS TAMBAHIN SPACE
    for line in f:
        if (line[:3]=="\'\'\'" or line[:3] == "\"\"\""):
            if (comment_flag):
                comment_flag = False
            else:
                comment_flag = True
        elif (line[0] != "#" and not comment_flag):
            data += (line + " ")

    #LANGKAH 1 : HAPUS SEMUA RESERVED WORDS
    temp = data
    for key in (list(reserved_words.keys())):
        temp = re.sub(r'\b' + key +r'\b', EMPTY_STRING, temp)
    #LANGKAH 2 : HAPUS SEMUA OPERATOR
    for e in (operators + mandatory_sym):
        temp = temp.replace(e," ")
    #LANGKAH 3 : DAPATKAN SEMUA VARIABLE DAN KONSTANT. ANGGAP NAMA DEF DAN IMPORT SEBAGAI VARIABLE JUGA EHE, DAN STRING DIANGGAP SEBAGAI CONST
    temp2 = temp.replace("\n","")
    temp2 = temp2.split(" ")
    temp2 = [x for x in temp2 if x] #berisi semua data var dan konst
    VARIABLES = copy.copy(temp2)

    #LANGKAH 4 : REPLACE SEMUA VAR DAN CONST SESUAI DENGAN STRING YG COCOK
    #LANGKAH 4.5 : CATAT STRING KARENA TAKUTNYA ADA YANG NGGA KE REPLACE
    string_thing = []
    for e in temp2 :
        if (variable_or_const_check(e)):
            replacement = CONTS_STRING
            if ((e[0]=="\"" or e[0]=="\'") and (e[len(e)-1]=="\"" or e[len(e)-1]=="\'")):
                string_thing.append(e)
        else:
            replacement = VAR_STRING
        data = re.sub(r'\b' + e +r'\b', replacement, data)

    #LANGKAH 4.8 : RUBAH STRING
    for e in string_thing :
        data = data.replace(e, CONTS_STRING)
    
    #LANGKAH 5 : REPLACE OPERATORS_SUBSTITUTE
    for e in operators_substitute.keys() :
        data = re.sub(r'\b' + e + r'\b', " "+ operators_substitute[e] +" ", data)

    #LANGKAH 6 : REPLACE RESERVED_WORDS
    for e in reserved_words.keys() :
        data = re.sub(r'\b' + e + r'\b', reserved_words[e], data)

    #LANGKAH 7 : HAPUS SPASI DAN NEWLINE AGAR MEMPERMUDAH PENGECEKAN
    data = data.replace(" ","")
    data = data.replace("\n",NEWLINE_CONST)

    data += "@."
    #print(data)
    invalid = []
    for var in VARIABLES:
        if (not variable_name_fa(var) and not variable_or_const_check(var)):
            invalid.append(var)
    if len(invalid) > 0:
        print("Syntax Error")
        print("Invalid variable(s) name : ",end="")
        for i in range(len(invalid)):
            if (i == len(invalid) -1):
                print(invalid[i])
            else:
                print(invalid[i], end= ", ")
        quit()

    
    return data