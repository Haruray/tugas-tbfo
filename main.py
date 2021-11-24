from cfg import CFG
from read_input import *
"""
Hanya support comment dalam bentuk
==============
\"\"\" test
\"\"\"
==============
atau
==============
#tes
==============
contoh input file ada di test.py
"""
grammar = CFG("grammar.txt")
grammar.cnf_convert()
print("Masukkan nama file yang akan dicompile (contoh penulisan : \'test.py\') : ", end="")
filename = input()
grammar.input_check(process_input(filename))
