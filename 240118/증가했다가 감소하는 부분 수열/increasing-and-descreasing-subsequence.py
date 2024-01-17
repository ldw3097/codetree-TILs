import sys
input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().split()))

def findlongest(start, end):
    ret = 1
    dp = [-1]*n
    dp[start] = 1
    progress = 1 if start<end else -1
    for i in range(start+progress, end, progress):
        parret = -1
        for j in range(start, i, progress):
            if arr[j] > arr[i]:
                parret = max(parret, dp[j])
        if parret != -1:
            dp[i] = parret + 1
            ret = max(ret, parret+1)
    return ret

ret = 0
for i in range(n):
    left = findlongest(i, -1)
    right = findlongest(i, n)
    ret = max(ret, left+right-1)
print(ret)