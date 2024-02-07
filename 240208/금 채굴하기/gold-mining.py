from collections import deque

n, m = map(int, input().split())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))

def calcearn(y, x, k):
    dq = deque()
    
    dq.append((y,x, k))
    visited = {(y,x)}
    cost = k*k + (k+1)*(k+1)
    ret = 0
    while dq:
        y,x, k = dq.popleft()
        if arr[y][x] == 1:
            ret += 1
        if k > 0:
            for dy,dx in zip((1,-1,0,0), (0,0,1,-1)):
                ny,nx = y+dy, x+dx
                if 0<=ny<n and 0<=nx<n and (ny,nx) not in visited:
                    visited.add((ny,nx))
                    dq.append((ny, nx, k-1))
    if ret*m >= cost:
        return ret
    return -1

ret = 0
for k in range(0, n+1):
    for y in range(n):
        for x in range(n):
            ret = max(ret, calcearn(y,x,k))
print(ret)