import sys
input = sys.stdin.readline
from collections import *
n, m = map(int, input().split())
arr = []
dp = [[987654321]*n for _ in range(n)]
dq = deque()
for i in range(n):
    arr.append( list(map(int, input().split())) )
    for j in range(n):
        if arr[i][j] == 2:
            dp[i][j] = 0
            dq.append((i,j))

while dq:
    y, x = dq.popleft()
    val = dp[y][x]
    for dy,dx in zip((1,-1,0,0), (0,0,1,-1)):
        ny,nx = y+dy, x+dx
        if 0<=ny<n and 0<=nx<n and arr[ny][nx] == 1:
            arr[ny][nx] = 2
            dp[ny][nx] = val+1
            dq.append((ny,nx))

for y in range(n):
    for x in range(n):
        val = arr[y][x]
        if val == 0:
            print(-1, end=" ")
        elif val == 1 and dp[y][x] == 987654321:
            print(-2, end=" ")
        else:
            print(dp[y][x], end=" ")
    print()