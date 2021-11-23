import re
from typing import final

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
    "raise" : "v"
    }
mandatory_sym = [":"]
operators = ["+", "-", "/", "*", ">", ">=", "<=", "<", "==", "!=", "and","or", "not", "+=", "-=", "%"]
EMPTY_STRING = ""
VAR_STRING = "/"
CONTS_STRING = "|"

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
    global reserved_words, mandatory_sym, operators,EMPTY_STRING,VAR_STRING
    f = open(filename, 'r')
    data = f.read()

    #LANGKAH 1 : HAPUS SEMUA RESERVED WORDS
    temp = data
    for key in (list(reserved_words.keys()) + mandatory_sym):
        temp = re.sub(r'\b' + key +r'\b', EMPTY_STRING, temp)
    #LANGKAH 2 : HAPUS SEMUA OPERATOR
    for e in (operators + mandatory_sym):
        temp = temp.replace(e,EMPTY_STRING)
    #LANGKAH 3 : DAPATKAN SEMUA VARIABLE DAN KONSTANT. ANGGAP NAMA DEF DAN IMPORT SEBAGAI VARIABLE JUGA EHE, DAN STRING DIANGGAP SEBAGAI CONST
    temp2 = temp.replace("\n","")
    temp2 = temp2.split(" ")
    temp2 = [x for x in temp2 if x] #berisi semua data var dan konst

    #LANGKAH 4 : REPLACE SEMUA VAR DAN CONST SESUAI DENGAN STRING YG COCOK
    for e in temp2 :
        if (variable_or_const_check(e)):
            replacement = CONTS_STRING
        else:
            replacement = VAR_STRING
        data = re.sub(r'\b' + e +r'\b', replacement, data)
    #print(temp2)
    #print(data)

    #LANGKAH 5 : HAPUS SPASI DAN NEWLINE AGAR MEMPERMUDAH PENGECEKAN
    data = data.replace(" ","")
    data = data.replace("\n","@")
    #print(data)
    return data