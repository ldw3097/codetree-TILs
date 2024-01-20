m = int(input())
a, b = map(int, input().split())

def search(i):
    minval, maxval = 1, m 
    guess= (1+m)//2
    ret = 1
    while guess != i:
        if guess > i:
            maxval = guess-1
        else:
            minval = guess+1
        guess = (maxval + minval) // 2
        ret += 1
    return ret

minval = 987654321
maxval = -1
for i in range(a, b+1):
    val = search(i)
    minval = min(minval, val)
    maxval = max(maxval, val)
print(minval, maxval)