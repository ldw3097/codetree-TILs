a = input()

def rle(s):
    ret = 0
    lastest = ""
    for c in s:
        if lastest != c:
            ret+=2
            lastest = c
    return ret

def rotate(s):
    return s[1:] + s[0]

minval = 99999
for i in range(len(a)):
    minval = min(minval, rle(a))
    a = rotate(a)
print(minval)