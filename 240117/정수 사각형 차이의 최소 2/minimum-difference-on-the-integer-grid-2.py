import sys
input = sys.stdin.readline
n = int(input())
arr = []
for i in range(n):
    arr.append( list(map(int, input().split()))  )

minval = 999
for minimum in range( 1, 101):
    if arr[n-1][n-1] < minimum:
        continue
    dp = [[999]*n for _ in range(n)]
    dp[n-1][n-1] = arr[n-1][n-1]
    for y in range(n-1, -1, -1):
        for x in range(n-1, -1, -1):
            if arr[y][x] < minimum or (y==n-1 and x == n-1):
                continue
            down = right = 999
            if x < n-1 and dp[y][x+1] != 999:
                right = dp[y][x+1]
            if y < n-1 and dp[y+1][x] != 999:
                down = dp[y+1][x]
            dp[y][x] = max(arr[y][x], min(down, right))
    if dp[0][0] != 999:
        minval = min(dp[0][0] - minimum, minval) 
print(minval)