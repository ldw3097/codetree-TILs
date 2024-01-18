import sys
input = sys.stdin.readline
from copy import *
n = int(input())
arr = []
for i in range(n):
    arr.append( list(map(int, input().split()))  )

arr2 = []
for i in range(n):
    toadd = []
    for j in range(n-1, -1, -1):
        toadd.append(arr[j][i])
    arr2.append(toadd)

def explode(x, y, arr):
    b = arr[x][y]
    arr[x][y] = -1
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]
    for i in range(1, b):
        for j in range(4):
            nx = x + dx[j]*i
            ny = y + dy[j]*i
            if 0<=nx<n and 0<=ny<n:
                arr[nx][ny] = -1
    for x in range(n):
        for y in range(n-1, -1, -1):
            if arr[x][y] == -1:
                arr[x].pop(y)
    ret = 0
    for x in range(n):
        for y in range(len(arr[x])-1, 0, -1):
            if arr[x][y] == arr[x][y-1]:
                ret += 1
    for x in range(n-1):
        for y in range(min(len(arr[x]), len(arr[x+1]))-1, -1, -1):
            if arr[x][y] == arr[x+1][y]:
                ret += 1
    return ret

ret = 0
for x in range(n):
    for y in range(n):
        ret = max(ret, explode(x, y, deepcopy(arr2)))
print(ret)