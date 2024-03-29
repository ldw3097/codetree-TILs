n, m = map(int, input().split())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))

def traverse(y, x, visited):
    if (y,x) == (n-1, m-1):
        return 1
    for dy, dx in zip((1, 0), (0,1)):
        ny,nx = y+dy, x+dx
        if 0<=ny <n and 0<=nx<m and arr[ny][nx] == 1 and (ny,nx) not in visited:
            visited.add((ny,nx))
            if(traverse(ny,nx, visited)):
                return 1
    return 0

ret = traverse(0,0, {(0,0),})
print(ret)