exp = input()
alpha = ("a", "b", "c", "d", "e", "f")


def calc(dic):
    ret = dic[exp[0]]
    for i in range(1, len(exp), 2):
        operand = dic[exp[i+1]]
        if exp[i] == "+":
            ret += operand
        elif exp[i] == "-":
            ret -= operand
        else:
            ret *= operand
    return ret

def sol(whatalpha, dic):
    dics = []
    for i in range(1,5):
        diccopy = dic.copy()
        diccopy[alpha[whatalpha]] = i
        dics.append(diccopy) 

    if whatalpha == 5:
        return max([ calc(dics[i]) for i in range(4) ])
    
    return max([sol(whatalpha+1, dics[i]) for i in range(4)])

print(sol(0,{}))