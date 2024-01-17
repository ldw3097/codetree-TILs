import sys
input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().split()))

dp = [1]*n

for i in range(n):
    maxval = 0
    for j in range(i):
        if arr[j] >arr[i]:
            maxval = max(maxval, dp[j])
    dp[i] = maxval+1
print(max(dp))