import sys
input = sys.stdin.readline
n, m = map(int, input().split())
inf = 987654321
arr = [[inf]*(n+1) for _ in range(n+1)]
for i in range(1, n+1):
    arr[i][i] = 0
for _ in range(m):
    a, b, c = map(int, input().split())
    arr[a][b] = min(arr[a][b], c)

for i in range(1, n+1):
    for j in range(1, n+1):
        for k in range(1, n+1):
            if arr[j][k] > arr[j][i] + arr[i][k]:
                arr[j][k] = arr[j][i] + arr[i][k]

for i in range(1,n+1):
    for j in range(1,n+1):
        if arr[i][j] == inf:
            print(-1, end=" ")
        else:
            print(arr[i][j], end=" ")
    print()