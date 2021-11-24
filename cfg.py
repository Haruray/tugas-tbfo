class CFG:
    def __init__(self, filename):
        set_of_rules = []
        rule=[]

        #file read and fetching rules
        f = open(filename, "r")
        for rules in f :
            if (rules[:2] != "//" and rules[:2]!="\n"):
                if (rules[len(rules)-1:] == '\n'):
                    rules = rules[:len(rules)-1]
                temp = rules.split(" -> ")
                temp[1] = temp[1].split(" | ")
                #di split lagi
                for i in range(len(temp[1])):
                    temp[1][i] = temp[1][i].split(" ")
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

        
    def cnf_convert(self):
        dummy = 1
        for i in range(1, len(self.mapping)):
            for k in range(len(self.mapping[i])):
                while (len(self.mapping[i][k]) > 2):
                    new_rule = "DUMMY" + str(dummy)
                    dummy += 1
                    new_rule_target = []
                    for j in range(1,-1,-1):
                        new_rule_target.append(self.mapping[i][k][len(self.mapping[i][k])-1-j])
                        self.mapping[i][k].pop(len(self.mapping[i][k])-1-j)

                    self.non_terminal_count += 1
                    self.non_terminal[new_rule] = self.non_terminal_count
                    self.mapping.append([new_rule_target])
                    
                    
                    self.mapping[i][k].append(new_rule)
                

    def input_check(self, str):
        #algoritmanya berdasarkan pseudocode ini :
        #https://en.wikipedia.org/wiki/CYK_algorithm
        #komentar lebih lengkap kedepannya, ini masih coba coba
        str_len = len(str)
        character_limit = len(str)+self.non_terminal_count+1
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
                            #print("(syms[0], syms[1] : ",syms[0],syms[1])
                            b = self.non_terminal[syms[0]]
                            c = self.non_terminal[syms[1]]
                            if (table[k][j][b] and table[i - k][j+k][c]):
                                table[i][j][l] = True
                                break
        
        if (table[str_len][1][1]):
            print("Accepted")
        else:
            print("Syntax Error")
    
    def print_grammar(self):
        first = True
        for e in self.non_terminal.keys():
            print(e,"->",end=" ")
            for map in self.mapping[self.non_terminal[e]]:
                if first:
                    print(map, end="")
                    first = False
                else :
                    print(" |",map, end="")
            print()
            first = True
