import sys
input = sys.stdin.readline
n = int(input())
arr = []
for i in range(n):
    arr.append( list(map(int, input().split()))  )
dp = [[0]*n for i in range(n)]
dp[n-1][n-1] = arr[n-1][n-1]
for y in range(n-1, -1, -1):
    for x in range(n-1, -1, -1):
        if y==n-1 and x==n-1:
            continue
        down=right = 987654321
        if x < n-1:
            right = dp[y][x+1]
        if y < n-1:
            down = dp[y+1][x]
        dp[y][x] = max(arr[y][x], min(right, down))
print(dp[0][0])