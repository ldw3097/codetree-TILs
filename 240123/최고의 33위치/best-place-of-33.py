import sys
input = sys.stdin.readline
n = int(input())
arr = []
for _ in range(n):
    arr.append( list(map(int, input().split())) )

def search(y, x):
    ret = 0
    for i in range(3):
        for j in range(3):
            if arr[y+i][x+j] == 1:
                ret += 1
    return ret

ret = -1
for i in range(n-2):
    for j in range(n-2):
        ret = max(ret, search(i,j))
print(ret)