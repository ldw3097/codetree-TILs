import sys
from collections import *
input = sys.stdin.readline
n, m = map(int, input().split())
arr = list(map(int, input().split()))

invalid = 987654321
dp = [invalid]*(m+1)
dp[0] = 0
for a in arr:
    for i in range(m, a-1, -1):
        if dp[i-a] != invalid and dp[i-a]+1 < dp[i]:
            dp[i] = dp[i-a]+1
if dp[m] == invalid:
    print(-1)
else:
    print(dp[m])