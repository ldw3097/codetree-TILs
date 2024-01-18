import sys
from collections import *
input = sys.stdin.readline
n, m = map(int, input().split())
arr = []
arr = list(map(int, input().split()))

dp = [-1]*(m+1)
dp[0] = 0
for i in range(1, m+1):
    maxval = -1
    for coin in arr:
        if i-coin>=0 and dp[i-coin] != -1:
            maxval = max(maxval, dp[i-coin])
    if maxval != -1:
        dp[i] = maxval+1
print(dp[m])