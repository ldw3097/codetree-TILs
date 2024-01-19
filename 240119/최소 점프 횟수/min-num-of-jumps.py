import sys
input = sys.stdin.readline
from collections import *
n = int(input())
arr = list(map(int, input().split()))

inf = 987654321
dp = [inf]*n
dp[0] = 0
dq = deque([0])
while dq:
    a = dq.popleft()
    val = arr[a]
    for i in range(1, val+1):
        if a+i < n and dp[a+i] > dp[a] + 1:
            dp[a+i] = dp[a] + 1
            dq.append(a+i)
            

if dp[n-1] == inf:
    print(-1)
else:
    print(dp[n-1])