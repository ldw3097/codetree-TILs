import sys
from collections import *
input = sys.stdin.readline
n, m = map(int, input().split())
arr = list(map(int, input().split()))

dp = {0:0}
for a in arr:
    dp2 = {}
    for b in dp:
        if a+b <= m and ((a+b) not in dp or dp[b]+1 < dp[a+b]):
            dp2[a+b] = dp[b]+1
    dp.update(dp2)
if m not in dp:
    print(-1)
else:
    print(dp[m])