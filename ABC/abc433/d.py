from collections import defaultdict

N, M = map(int, input().split())
A = list(map(int, input().split()))

p10 = [1 % M]
for i in range(1, 11):
    p10.append(p10[-1] * 10 % M)

cnt = [defaultdict(int) for _ in range(11)]

rem = [0] * N  
dig = [0] * N 

for i, a in enumerate(A):
    r = a % M
    d = len(str(a))  
    rem[i] = r
    dig[i] = d
    cnt[d][r] += 1

ans = 0
for i in range(N):
    x = rem[i]
    for L in range(1, 11):
        t = (M - (x * p10[L]) % M) % M
        ans += cnt[L].get(t, 0)

print(ans)
