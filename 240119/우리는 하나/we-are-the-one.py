import sys
input = sys.stdin.readline
n,k,u,d = map(int, input().split())
arr = []
for _ in range(n):
    arr.append( list(map(int, input().split())) )


def traverse(y, x):
    val = arr[y][x]
    arr[y][x] = -1
    ret = 1
    
    for dy, dx in zip((1,-1,0,0), (0,0,1,-1)):
        ny = y+dy
        nx = x+dx
        if 0<=ny<n and 0<=nx<n and arr[ny][nx] != -1 and u <= abs(val - arr[ny][nx]) <= d:
            ret += traverse(ny, nx)
    return ret

blocks = []
for i in range(n):
    for j in range(n):
        if arr[i][j] != -1:
            blocks.append(traverse(i, j))
blocks.sort(reverse=True)
ret = sum(blocks[:k])
print(ret)