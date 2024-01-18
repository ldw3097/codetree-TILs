import sys
from collections import *
input = sys.stdin.readline
n, m = map(int, input().split())
arr = []
arr = list(map(int, input().split()))


dq = deque()
dq.append(0)
dp = [987654321]*(m+1)
dp[0] = 0
while dq:
    a = dq.popleft()
    b = dp[a]
    for coin in arr:
        if a+coin <= m and dp[a+coin] > b+1:
            dp[a+coin] = b+1
            dq.append(a+coin)
if dp[m] == 987654321:
    print(-1)
else:
    print(dp[m])