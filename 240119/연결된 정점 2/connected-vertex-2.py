import sys
input = sys.stdin.readline
n = int(input())
arr = [[0,1] for _ in range(100001)]
for i in range(100001):
    arr[i][0] = i

def find(a):
    if arr[a][0] == a:
        return a 
    root = find(arr[a][0])
    arr[a][0] = root 
    return root

def union(a, b):
    x = find(a)
    y = find(b)
    if x == y:
        return arr[x][1]
    arr[y][0] = x
    arr[x][1] += arr[y][1]
    return arr[x][1]
for _ in range(n):
    a,b = map(int, input().split())
    print(union(a,b))