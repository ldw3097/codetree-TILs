import sys
input = sys.stdin.readline
n, m = list(map(int, input().split()))
arr = []
for _ in range(n):
    arr.append( list(map(int, input().split()))  )

dp = [[0]*m for _ in range(n)]
dp[0][0] = 1
globalmax = 0
for i in range(n):
    for j in range(m):
        maxval = 0
        for k in range(i):
            for l in range(j):
                if arr[i][j] > arr[k][l]:
                    maxval = max(maxval, dp[k][l])
        if maxval != 0:
            dp[i][j] = maxval + 1
            globalmax = max(globalmax, dp[i][j])
print(globalmax)