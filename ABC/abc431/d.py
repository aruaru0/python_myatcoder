n = int(input())
w = []
h = []
b = []
t = 0 
sb = 0
for _ in range(n):
    wi, hi, bi = map(int, input().split())
    w.append(wi)
    h.append(hi)
    b.append(bi)
    t += wi
    sb += bi

c = t // 2  
ng = -10**18 
dp = [ng] * (c + 1)
dp[0] = 0

for i in range(n):
    wi = w[i]
    di = h[i] - b[i]
    if di <= 0: 
        continue
    for cur in range(c, wi - 1, -1): 
        v = dp[cur - wi] + di
        if v > dp[cur]:
            dp[cur] = v

best = max(dp) 
ans = sb + best
print(ans)



