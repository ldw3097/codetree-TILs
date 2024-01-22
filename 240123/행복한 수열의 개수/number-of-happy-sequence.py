import sys
input = sys.stdin.readline
n, m = map(int, input().split())
arr = []
for _ in range(n):
    arr.append( list(map(int, input().split())) )

def ishappy(y, x):
    a = 1
    b = 1
    if y == -1:
        for y in range(n-1):
            if arr[y][x] == arr[y+1][x]:
                a += 1
                b = max(a,b)
            else:
                a = 1
    elif x == -1:
        for x in range(n-1):
            if arr[y][x] == arr[y][x+1]:
                a+=1
                b = max(a,b)
            else:
                a = 1
    if b >= m:
        return True
    else:
        return False

ret = 0
for i in range(n):
    ret += ishappy(i, -1)
    ret += ishappy(-1,i)
print(ret)