import sys
input = sys.stdin.readline
n, m = map(int, input().split())
arr = []
for _ in range(m):
    arr.append( list(map(int, input().split())) )

inf = 987654321
dp = [inf]*(n+1)
dp[n] = 0
dp[0] = -1
for _ in range(n-1):
    for a, b, c in arr:
        if dp[a]+c < dp[b]:
            dp[b] = dp[a]+c
        if dp[b]+c < dp[a]:
            dp[a] = dp[b]+c
print(max(dp))