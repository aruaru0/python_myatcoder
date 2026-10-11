n, k, m = map(int, input().split())

a = list(map(int, input().split()))

k += m
tot = 0
for e in a :
    tot += (e+k-1)//k

print(tot)