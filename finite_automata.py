def variable_name_fa(var_name):
    """
    Fungsi FA pengecekan apakah nama sesuai aturan (tidak boleh angka di depan dan hanya terdiri atas alfanumerik : a-z, A-Z, angka, _)
    return true kalau benar, dan false sebaliknya
    """
    state = 0 #state awal
    accepting = {1} #state menerima
    reject = 2 #dead state
    meet_null = False #apakah bisa transisi atau tidak (ini aslinya nfa tapi aga males ngoding fullnya)
    transitions = {
    0 : {'1234567890' : 2, 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_' : 1},
    1 : {'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_1234567890':1},
    2 : {'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_1234567890':2}
}
    for c in var_name:
        for key in transitions[state].keys():
            if c in key : #apakah c (karakter dari string input) ada di salah satu key yang ada
                curr_key = key
                meet_null = False
                break
            else: #kalau tidak (berarti pakai simbol yang tidak diperbolehkan) maka akan masuk dead state
                meet_null = True
        if (not meet_null):
            state = transitions[state][curr_key]
        else:
            state = 2
            meet_null = False

    return (state in accepting) and reserved_word_check(var_name)

def reserved_word_check(var_name):
    """
    Fungsi FA pengecekan apakah nama variable termasuk ke reserved words atau tidak
    return true kalau variable tidak termasuk reserved words (variable yang diperbolehkan)
    return false kalau masuk ke reserved words
    """
    state = 0
    accept = 99
    reject = 100
    meet_null = False
    accepting = {accept}
    # reserved words yg dimasukkan : if, in, is, import, False, True, def, return, None, continue, for, class, from, while, and, not, with, as, elif, else, or, pass,
    # break, raise
    transitions = {
        0 : {'i' : 1, 'F' : 6, 'd': 10, 'r' : 12, 'N': 17, 'c':20, 'f': 27, 'T': 29, 'w' : 37, 'a' : 41, 'n' : 43, 'a' : 47, 'e' : 48, 'o': 51, 'p' : 52, 'b' : 55, 'r' : 59},
        1 : {'f' : accept, 'n': accept, 'm' : 2, 's': accept},
        2 : {'p' : 3},
        3 : {'o' : 4},
        4 : {'r' : 5},
        5 : {'t' : accept},
        6 : {'a' : 7},
        7 : {'l' : 8},
        8 : {'s' : 9},
        9 : {'e' : accept},
        10 : {'e' : 11},
        11 : {'f': accept},
        12 : {'e' : 13},
        13 : {'t' : 14},
        14 : {'u' : 15},
        15 : {'r' : 16},
        16 : {'n' : accept},
        17 : {'o' : 18},
        18 : {'n' : 19},
        19 : {'e' : accept},
        20 : {'o' : 21, 'l' :32},
        21 : {'n' : 22},
        22 : {'t' : 23},
        23 : {'i' : 24},
        24 : {'n' : 25},
        25 : {'u' : 26},
        26 : {'e' : accept},
        27 : {'o' : 28, 'r' : 35},
        28 : {'r' : accept},
        29 : {'r' : 30},
        30 : {'u' : 31},
        31 : {'e' : accept},
        32 : {'a' : 33},
        33 : {'s' : 34},
        34 : {'s': accept},
        35 : {'o' : 36},
        36 : {'m' : accept},
        37 : {'h' : 38, 'i' : 45},
        38 : {'i' : 39},
        39 : {'l' : 40},
        40 : {'e' : accept},
        41 : {'n' : 42},
        42 : {'d' : accept},
        43 : {'o' : 44},
        44 : {'t' : accept},
        45 : {'t' : 46},
        46 : {'h' : accept},
        47 : {'s' : accept},
        48 : {'l' : 49},
        49 : {'i' : 1, 's' : 50},
        50 : {'e' : accept},
        51 : {'r' : accept},
        52 : {'a' : 53},
        53 : {'s' : 54},
        54 : {'s' : accept},
        55 : {'r' : 56},
        56 : {'e' : 57},
        57 : {'a' : 58},
        58 : {'k' : accept},
        59 : {'a' : 60},
        60 : {'i' : 61},
        61 : {'s' : 62},
        62 : {'e' : accept},

        99 : {'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_1234567890' : reject},
        100 : {'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_1234567890' : reject}
    }

    for c in var_name:
        for key in transitions[state].keys():
            if c in key :
                curr_key = key
                meet_null = False
                break
            else: #jika tidak (berarti ada huruf yang tidak membentuk reserved words) berarti masuk ke dead state
                meet_null = True
        if ( not meet_null ):
            state = transitions[state][curr_key]
        else:
            state = reject
            meet_null = False

    return not (state in accepting)
