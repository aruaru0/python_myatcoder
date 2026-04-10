N, M = map(int, input().split())
s, t = map(int, input().split())

if M == 0 :
    p = [s]
else :
    p = [s] + list(map(int, input().split()))


bit = 1 << (M + 1)
inf = int(10**18)
dp = [[inf for _ in range(M+1)] for _ in range(bit)]

def idx2rc(idx) :
    idx-=1
    return idx//N, idx%N

for i in range(M+1) :
    r0, c0 = idx2rc(p[0])
    r1, c1 = idx2rc(p[i])
    d = abs(r0-r1) + abs(c0-c1)
    dp[1 | 1<<i][i] = d

for b in range(bit) :
    for _from in range(M+1) :
        if (b >> _from) & 1 == 0 :
            continue
        if dp[b][_from] == inf :
            continue
        for to_ in range(M+1) :
            if (b >> to_) & 1 == 1 :
                continue
            r0, c0 = idx2rc(p[_from])
            r1, c1 = idx2rc(p[to_])
            d = abs(r0-r1) + abs(c0-c1)
            dp[b | 1<<to_][to_] = min(dp[b | 1<<to_][to_], dp[b][_from] + d)
        

ans = inf
for i in range(M+1) :
    r0, c0 = idx2rc(p[i])
    r1, c1 = idx2rc(t)
    d = abs(r0-r1) + abs(c0-c1)
    ans = min(ans, dp[bit-1][i] + d)

print(ans)