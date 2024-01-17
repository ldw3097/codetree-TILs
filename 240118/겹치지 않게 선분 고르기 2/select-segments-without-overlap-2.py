import sys
input = sys.stdin.readline
n = int(input())
arr = []
for i in range(n):
    arr.append( list(map(int, input().split()))  )

arr.sort()
dp = [0]*1001
for a,b in arr:
    parmax = 0
    for i in range(a):
        parmax = max(parmax, dp[i])
    dp[b] = parmax+1

print(max(dp))