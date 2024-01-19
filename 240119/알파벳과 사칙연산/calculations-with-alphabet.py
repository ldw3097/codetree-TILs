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
    dic1 = dic.copy()
    dic1[alpha[whatalpha]] = 1
    dic2 = dic.copy()
    dic2[alpha[whatalpha]] = 4
    if whatalpha == 5:
        return max(calc(dic1), calc(dic2))
    ret1 = sol(whatalpha+1, dic1)
    ret2 = sol(whatalpha+1, dic2)
    return max(ret1, ret2)

print(sol(0,{}))