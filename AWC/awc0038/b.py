n, k = map(int, input().split())

d = list(map(int, input().split()))
d.sort()

total, tot_k = 0,0
for i in range(n) :
    if i < k :
        tot_k += d[i]
    total += d[i]

print(total - tot_k)