import sys
input = sys.stdin.readline
from itertools import *
n = int(input())
arr = []
for _ in range(n):
    arr.append( list(map(int, input().split())) )

def calc(perm):
    ret=98765321
    for i, val in enumerate(perm):
        ret = min(ret, arr[i][val])
    return ret

perms = permutations(range(n), n)
ret=0
for perm in perms:
    ret = max(ret, calc(perm))
print(ret)