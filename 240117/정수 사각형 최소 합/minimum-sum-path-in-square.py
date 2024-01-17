import sys
input = sys.stdin.readline
n = int(input())
arr = []
for i in range(n):
    arr.append( list(map(int, input().split()))  )
dp = [[0]*n for i in range(n)]
for i in range(n):
    for j in range(n-1, -1, -1):
        dp[i][j] = arr[i][j]
        if i == 0 and j == n-1:
            continue
        up = right = 987654321
        if i > 0:
            up = dp[i-1][j]
        if j < n-1:
            right = dp[i][j+1]
        dp[i][j] += min(up,right)
print(dp[n-1][0])