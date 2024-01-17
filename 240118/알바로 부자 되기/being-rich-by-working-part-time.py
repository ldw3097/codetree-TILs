import sys
input = sys.stdin.readline
n = int(input())
arr = []
for i in range(n):
    arr.append( list(map(int, input().split()))  )

dp = [0]*1001
for a,b,c in arr:
    parmax = 0
    for i in range(a):
        parmax = max(parmax, dp[i])
    dp[b] = parmax+c

print(max(dp))