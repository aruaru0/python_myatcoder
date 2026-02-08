N, K = map(int, input().split())
sN = str(N)
L = len(sN)

dp = [[0]*2 for _ in range(K+1)]
dp[0][1] = 1 

for i in range(L):
    nd = int(sN[i]) 
    ndp = [[0]*2 for _ in range(K+1)]

    for sm in range(K+1):
        # N と同じ桁まで一致している
        for dgt in range(nd+1): # 0~ndまでループ
            nsm = sm + dgt
            if nsm > K: break
            nt = 1 if dgt == nd else 0
            ndp[nsm][nt] += dp[sm][1]

        # すでに N より小さい
        for dgt in range(10): # 0 ~ 9までループ
            nsm = sm + dgt
            if nsm > K: break
            ndp[nsm][0] += dp[sm][0]

    dp = ndp

ans = dp[K][0] + dp[K][1]
print(ans)

