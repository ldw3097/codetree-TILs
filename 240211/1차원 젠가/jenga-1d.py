n = int(input())
arr = []
for _ in range(n):
    arr.append(int(input()))
for _ in range(2):
    a, b = map(int, input().split())
    arr[a-1: b] = []

print(len(arr))
for n in arr:
    print(n)