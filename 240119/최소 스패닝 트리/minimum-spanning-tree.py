import sys
input = sys.stdin.readline
sys.setrecursionlimit(10*7)
n, m = tuple(map(int, input().split()))
edges = []
edges = [
    tuple(map(int, input().split()))
    for _ in range(m)
]

uf = [0]*(n + 1)


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
    
for i in range(1, n + 1):
    uf[i] = i
    
edges.sort(key=lambda x : x[2])
ret = 0
for a,b,c in edges:
    if find(a) != find(b):
        ret += c
        union(a,b)
print(ret)