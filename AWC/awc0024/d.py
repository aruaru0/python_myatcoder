n, w, k = map(int, input().split())

p = [0] * (n+1)
for _ in range(k) :
    l = int(input()) - 1
    r = min(n, l+w)
    p[l]+=1
    p[r]-=1

for i in range(n) :
    p[i+1] += p[i]


print(*p[:n])