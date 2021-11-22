from cfg import CFG
from read_input import *
"""
BACA INI!!!
untuk sementara, grammar dan pemrosesan hanya menghandle bentuk if var > var : (newline)
dan berhasil. rule sederhana berada di grammar2.txt
contoh input file ada di test.py
"""
grammar = CFG("grammar2.txt")
grammar.input_check(process_input('test.py'))
#grammar.input_check("a/>/:@")
#grammar.input_check("aab")
