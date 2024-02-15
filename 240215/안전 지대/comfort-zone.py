import sys
sys.setrecursionlimit(10**6)

n, m = map(int, input().split())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))

retk = -1
retcomf = -1

def traverse(y,x,visited,k):
    visited.add((y,x))
    for dy,dx in zip((1,-1,0,0),(0,0,1,-1)):
        ny,nx = y+dy,x+dx
        if 0<=ny<n and 0<=nx<m and arr[ny][nx]>k and (ny,nx) not in visited:
            traverse(ny,nx,visited,k)
    
def getcomf(k):
    visited = set()
    ret = 0
    for y in range(n):
        for x in range(m):
            if arr[y][x] > k and (y,x) not in visited:
                ret += 1
                traverse(y,x,visited, k)
    return ret

for k in range(1,100):
    comf = getcomf(k)
    if comf > retcomf:
        retk = k
        retcomf = comf
    if comf == 0:
        break
    
print(f"{retk} {retcomf}")