import sys
input = sys.stdin.readline
n = int(input())
arr = []
for i in range(n):
    arr.append( list(map(int, input().split()))  )
dp = [[0]*n for i in range(n)]
dp[0][0] = arr[0][0]
for i in range(n):
    for j in range(n):
        if i==0 and j==0:
            continue
        a=-1
        if i>0:
            a = dp[i-1][j]
        if j>0:
            a = max(a, dp[i][j-1])
        dp[i][j] = min(arr[i][j], a)
print(dp[n-1][n-1])