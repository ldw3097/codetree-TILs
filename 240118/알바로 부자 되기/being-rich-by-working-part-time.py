import sys
input = sys.stdin.readline
n = int(input())
arr = []
for i in range(n):
    arr.append( list(map(int, input().split()))  )

enddaytomoney = {}

for a,b,c in arr:
    parmax = 0
    for endday in enddaytomoney:
        if endday < a:
            parmax = max(parmax, enddaytomoney[endday])
    enddaytomoney[b] = parmax+c

print(max(enddaytomoney.values()))