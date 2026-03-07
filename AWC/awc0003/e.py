
n, m = map(int, input().split())
w = list(map(int, input().split()))
c = list(map(int, input().split()))

c.sort(reverse=True)
c = c[:n]

sum_w = [0] * (1 << n)
for s in range(1 << n):
    total = 0
    for i in range(n):
        if (s >> i) & 1:
            total += w[i]
    sum_w[s] = total

dp = [False] * (1 << n)
dp[0] = True

for limit in c:
    tmp = dp[:]
    
    for s in range(1 << n):
        if not dp[s]:
            continue
        
        rest = ((1 << n) - 1) ^ s
        
        sub = rest
        while sub > 0:
            if not tmp[s | sub] and sum_w[sub] <= limit:
                tmp[s | sub] = True
            sub = (sub - 1) & rest
            
    dp = tmp

if dp[(1 << n) - 1]:
    print("Yes")
else :
    print("No")

