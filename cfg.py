class CFG:
    def __init__(self, filename):
        set_of_rules = []
        rule=[]

        #file read and fetching rules
        f = open(filename, "r")
        for rules in f :
            if (rules[len(rules)-1:] == '\n'):
                rules = rules[:len(rules)-1]
            temp = rules.split(" -> ")
            temp[1] = temp[1].split(" | ")
            set_of_rules.append(temp)

        grammar = set_of_rules
        self.non_terminal_count = 0
        self.non_terminal = {}
        

        #Mapping non terminal syms
        #setiap non terminal di hubungkan dengan urutan angkanya
        for production_rule in grammar:
            self.non_terminal_count +=1
            self.non_terminal[production_rule[0]] = self.non_terminal_count
        
        #mapping syms
        #mendata arah transisi
        self.mapping = ["notvalid" for i in range(self.non_terminal_count+1)]
        for production_rule in grammar:
            self.mapping[self.non_terminal[production_rule[0]]] = production_rule[1]

    def input_check(self, str):
        #algoritmanya berdasarkan pseudocode ini :
        #https://en.wikipedia.org/wiki/CYK_algorithm
        #komentar lebih lengkap kedepannya, ini masih coba coba
        str_len = len(str)
        character_limit = 100
        table = [[[False for i in range(character_limit)] for j in range(character_limit)] for i in range (self.non_terminal_count)]

        for i in range(1,str_len+1):
            for j in range(1, self.non_terminal_count+1):
                for k in self.mapping[j]:
                    if (k[0] == str[i-1]):
                        table[1][i][j] = True
                        break

        for i in range (2, str_len+1):
            for j in range(1, str_len-i+1 +1):
                for k in range(1, i-1 +1):
                    for l in range(1, self.non_terminal_count+1):
                        for syms in self.mapping[l]:
                            if (len(syms)==1):
                                continue
                            b = self.non_terminal[syms[0]]
                            c = self.non_terminal[syms[1]]
                            if (table[k][j][b] and table[i - k][j+k][c]):
                                table[i][j][l] = True
                                break
        
        if (table[str_len][1][1]):
            print("Accepted")
        else:
            print("Not accepted")