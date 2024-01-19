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
    X = find(a)
    Y = find(b)
    uf[X] = Y

edges.sort(key=lambda x : x[2])
for i in range(1, n + 1):
    uf[i] = i

ans = 0
for x,y,cost in edges:
    if find(x) != find(y):
        ans += cost
        union(x,y)
print(ans)