import sys
input = sys.stdin.readline
n, m = map(int, input().split())
arr = []
for _ in range(n):
    arr.append( tuple(map(int, input().split())) )

dp = [[-1]*m for _ in range(n)]
for i in range(m):
    dp[0][i] = arr[0][i]
for i in range(1,n):
    for j in range(m):
        dp[i][j] = max(*dp[i-1][:j], *dp[i-1][j+1:])+arr[i][j]
print(max(dp[n-1]))