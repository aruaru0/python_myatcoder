from collections import defaultdict

n = int(input())

d = defaultdict(int)
for e in list(map(int, input().split())) :
    d[e] += 1

tot = 0
for e in d.values() :
    tot += e * (e-1) // 2

print(tot)
