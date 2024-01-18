import sys
input = sys.stdin.readline
n = int(input())
arr = []
for i in range(n):
    arr.append( list(map(int, input().split()))  )
arr.sort(key=lambda x: x[1])
enddaytomoney = {}

for a,b,c in arr:
    parmax = 0
    for endday in enddaytomoney:
        if endday < a:
            parmax = max(parmax, enddaytomoney[endday])
    if b not in enddaytomoney:
        enddaytomoney[b] = parmax+c
    else:
        enddaytomoney[b] = max(enddaytomoney[b], parmax+c)

print(max(enddaytomoney.values()))