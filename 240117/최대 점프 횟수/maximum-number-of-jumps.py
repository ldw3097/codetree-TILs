import sys
input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().split()))

dp = [-1]*n
dp[0] = 0
for i in range(1,n):
    maxval = -1
    for j in range(i):
        if i-j <= arr[j]:
            maxval = max(maxval, dp[j])
    if maxval >=0:
        dp[i] = maxval+1
print(max(dp))