from cfg import CFG
f = open("grammar.txt", "r")
set_of_rules = []
rule=[]

for rules in f :
    if (rules[len(rules)-1:] == '\n'):
        rules = rules[:len(rules)-1]
    temp = rules.split(" -> ")
    temp[1] = temp[1].split(" | ")
    set_of_rules.append(temp)

grammar = CFG(set_of_rules)
grammar.input_check("cock")
