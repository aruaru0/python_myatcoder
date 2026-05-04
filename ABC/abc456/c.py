S = input().strip()
MOD = 998244353
ans = 0
cur = 0

for i, c in enumerate(S):
    if i > 0 and c == S[i-1]:
        cur = 1
    else:
        cur += 1
    ans += cur

print(ans % MOD)
