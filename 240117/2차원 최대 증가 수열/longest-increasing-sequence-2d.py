import sys
input = sys.stdin.readline
n, m = map(int, input().split())
arr = []
for _ in range(n):
    arr.append( list(map(int, input().split()))  )

dp = [[0]*m for _ in range(n)]
globalmax = 0
for i in range(n):
    for j in range(m):
        maxval = 0
        for k in range(i):
            for l in range(j):
                if arr[i][j] > arr[k][l]:
                    maxval = max(maxval, dp[k][l])
        dp[i][j] = maxval + 1
        globalmax = max(globalmax, dp[i][j])
print(globalmax)