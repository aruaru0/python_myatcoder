n, q = map(int, input().split())
k = list(map(int, input().split()))

p = [i+1 for i in range(n)]

for i in range(q) :
    x = k[i]
    for j in range(x):
        p[j] = -p[j]
    for j in range(x//2):
        p[j], p[x-1-j] = p[x-1-j], p[j]

print(*p, sep="\n")