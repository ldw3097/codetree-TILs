import sys
from collections import *
input = sys.stdin.readline
n, m, t = map(int, input().split())
arr = {}
direction = {"D" : (1,0), "U" : (-1,0), "R":(0,1), "L":(0,-1)}
for i in range(m):
    r,c,d,w = input().split()
    r,c,w = int(r), int(c), int(w)
    arr[(r,c)] = (i, direction[d], w)

def ballmove(r,c, newarr):
    i, d, w = arr[(r,c)]
    ny, nx = r+d[0], c+d[1]
    if ny <= 0 or ny > n:
        ny = r 
        d = (d[0]*-1, 0)
    if nx <= 0 or nx > n:
        nx = c
        d = (0, d[1]*-1)
    newarr[(ny,nx)].append((i, d, w))

def combine(newarr):
    arr2 = {}
    for r,c in newarr:
        if len(newarr[(r,c)]) == 1:
            arr2[(r,c)] = newarr[(r,c)][0]
        else:
            newi = -1
            neww = 0
            for i,d,w in newarr[(r,c)]:
                if i > newi:
                    newd = d 
                    newi = i 
                neww += w
            arr2[(r,c)] = (newi, newd, neww)
    global arr
    arr = arr2

def allmove():
    newarr = defaultdict(list)
    for r,c in arr:
        ballmove(r,c, newarr)
    combine(newarr)

for _ in range(t):
    allmove()
print(len(arr), end=" ")
maxw = -1
for i, d, w in arr.values():
    maxw = max(maxw, w)
print(maxw)