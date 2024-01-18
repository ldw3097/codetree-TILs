a = input()

def rle(s):
    ret = -2
    lastest = ""
    lastnum = 0
    for c in s:
        if lastest != c:
            ret += (2 + lastnum//10)
            lastest = c
            lastnum = 1
        else:
            lastnum += 1
    ret += (2 + lastnum//10)
    return ret

def rotate(s):
    return s[1:] + s[0]

minval = 99999
for i in range(len(a)):
    minval = min(minval, rle(a))
    a = rotate(a)
print(minval)