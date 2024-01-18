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
    arr[b] = a

for i in range(m):
    a,b,c = map(int, input().split())
    if a == 1:
        print(int(find(b) == find(c)))
    else:
        union(b,c)