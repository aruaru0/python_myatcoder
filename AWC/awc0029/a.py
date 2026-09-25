n, p, b, k = map(int, input().split())
c = list(map(int, input().split()))

tot = 0
for e in c:
    if e < k :
        tot += e * p
    else :
        tot += e * (p + b)

print(tot)