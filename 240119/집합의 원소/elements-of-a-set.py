import sys
input = sys.stdin.readline
n, m = map(int, input().split())
arr = [0] * (n+1)
for i in range(n+1):
    arr[i] = i

def find(a):
    if a == arr[a]:
        return a
    root = find(arr[a])
    arr[a] = root
    return root

def union(a, b):
    x = find(a)
    y = find(b)
    if x == y:
        return
    arr[x] = y

for _ in range(m):
    a,b,c = map(int, input().split())
    if a == 1:
        print(int(find(b) == find(c)))
    else:
        union(b,c)