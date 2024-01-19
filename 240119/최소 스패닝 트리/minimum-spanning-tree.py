import sys
input = sys.stdin.readline
sys.setrecursionlimit(10*7)
n, m = map(int, input().split())
arr = []
for _ in range(m):
    arr.append( list(map(int, input().split())) )

uf = [0]*(n + 1)
for i in range(n + 1):
    uf[i] = i

def find(a):
    if uf[a] == a:
        return a 
    root = find(uf[a])
    uf[a] = root
    return root 

def union(a,b):
    x = find(a)
    y = find(b)
    uf[b] = a
    

arr.sort(key=lambda x : x[2])
ret = 0
for a,b,c in arr:
    if find(a) != find(b):
        ret += c
        union(a,b)
print(ret)