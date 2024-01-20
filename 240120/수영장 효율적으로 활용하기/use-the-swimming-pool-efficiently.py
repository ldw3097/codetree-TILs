import sys
input = sys.stdin.readline
n, m = map(int, input().split())
arr = list(map(int, input().split()))

def isable(maxtime):
    lane = 0
    timeleft = maxtime
    for t in arr:
        if t > timeleft:
            lane += 1
            timeleft = maxtime
            if lane >= m:
                return False
        timeleft -= t 
    return True

minval = max(arr)
maxval = 1440*100000
while minval < maxval:
    mid = (minval + maxval)//2
    if isable(mid):
        maxval = mid
    else:
        minval = mid+1
print(maxval)