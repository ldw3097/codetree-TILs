n = int(input())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))
y,x = map(int, input().split())
y,x = y-1, x-1

num = arr[y][x]
arr[y][x] = -1
for dy,dx in zip((1,-1,0,0), (0,0,1,-1)):
    for i in range(1,num):
        ny = y + dy * i
        nx = x + dx * i 
        if ny >= n or ny < 0 or nx >=n or nx <0 :
            break
        arr[ny][nx] = -1

newarr = [[0] * n for _ in range(n)]
for x in range(n):
    arry = n-1
    for y in range(n-1, -1, -1):
        if arr[y][x] != -1:
            newarr[arry][x] = arr[y][x]
            arry -= 1

for y in range(n):
    for x in range(n):
        print(newarr[y][x], end=" ")
    print()