import sys
input = sys.stdin.readline
from itertools import *
n, m = map(int,input().split())
def dist2(x1,x2,y1,y2):
    return (x1-x2)**2 + (y1-y2)**2

arr = [[0]*n for _ in range(n)]
dot = []
for i in range(n):
    a, b = map(int, input().split())
    for j, (da, db) in enumerate(dot):
        distance = dist2(a,da,b,db)
        arr[i][j] = distance
        arr[j][i] = distance
    dot.append((a,b))

def calcmaxlength(dots):
    ret = 0
    twodot = combinations(dots, 2)
    for dot1, dot2 in twodot:
        ret = max(ret, arr[dot1][dot2])
    return ret

picking = combinations(range(n), m)
ret = 987654321
for dots in picking:
    ret = min(ret, calcmaxlength(dots))
print(ret)