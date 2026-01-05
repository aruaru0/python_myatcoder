import math

n = int(input())

a = [i*i for i in range(1, math.isqrt(n)+1)]


m = [0] * (n+1)

for i in range(0, len(a)) :
    for j in range(i+1, len(a)):
        if a[i] + a[j] <= n:
            m[a[i] + a[j]] += 1
        

ans = []
for i in range(0, len(m)) :
    if m[i] == 1 : ans.append(i)

print(len(ans))
print(*ans)