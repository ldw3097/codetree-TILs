import sys
input = sys.stdin.readline
n = int(input())
arr = []
for i in range(n):
    arr.append( list(map(int, input().split()))  )
dp = [[0]*n for i in range(n)]

for i in range(n):
    for j in range(n):
        up = left = 0
        if i>0:
            up = dp[i-1][j]
        if j>0:
            left = dp[i][j-1]
        dp[i][j] = arr[i][j] + max(up, left)
print(dp[n-1][n-1])