import sys
input = sys.stdin.readline
n, m = map(int, input().split())
arr = []
for _ in range(m):
    arr.append( list(map(int, input().split())) )

uf = [0]*10001
for i in range(10001):
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
    if x == y:
        return False
    uf[a] = b
    return True

arr.sort(key=lambda x : x[2])
ret = 0
for a,b,c in arr:
    if union(a,b):
        ret += c
print(ret)