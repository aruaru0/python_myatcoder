n, k = map(int, input().split())
a = list(map(int, input().split()))

m = [0]*k
for e in a :
    m[e-1] += 1

mx = max(m)

cnt = 0
for e in m:
    if e >= mx-1 : cnt+=1

print(cnt)