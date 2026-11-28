N, M, K = map(int, input().split())
P = list(map(int, input().split()))
G = [1<<i for i in range(N)]
for _ in range(K):
  u, v = map(int, input().split())
  u -= 1
  v -= 1
  G[u] |= 1<<v
  G[v] |= 1<<u

N1 = N // 2
N2 = N - N1

# 前半
mask = (1<<N1) - 1
memo = [0] * (1<<N1)
for s in range(1, 1<<N1):
  i = len(bin(s)) - 3
  memo[s] = max(memo[s ^ (1<<i)], memo[s & ~G[i] & mask] + P[i])

ans = max(memo)
# 後半
memo2 = [0] * (1<<N2)
ng = [0] * (1<<N2)
for s in range(1, 1<<N2):
  i = len(bin(s))-3
  memo2[s] = max(memo2[s ^ (1<<i)], memo2[s & ~(G[i+N1]>>N1)] + P[i+N1])
  ng[s] = ng[s^(1<<i)] | G[i+N1]
  ans = max(ans, memo2[s] + memo[~ng[s] & mask])

print(min(M, ans))
