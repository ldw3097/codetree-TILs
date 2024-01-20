import sys
input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().split()))

def solve(arr):
    s = sum(arr)
    if s%2 == 1:
        print("No")
        return
    s //= 2
    dp = [0] *(s+1)
    dp[0] = 1
    for a in arr:
        for i in range(s, a-1, -1):
            if dp[i-a] == 1:
                dp[i] = 1
    if dp[s] == 1:
        print("Yes")
    else:
        print("No")

    

solve(arr)