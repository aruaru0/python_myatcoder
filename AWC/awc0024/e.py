from collections import deque

n, w = map(int, input().split())
BIG = 1 << 30
dp = [BIG] * (w + 1)
dp[0] = 0

best = {}
for _ in range(n):
    l, c = map(int, input().split())
    best[l] = best.get(l, 0) + c

for l, c in best.items():
    if c * l >= w:
        for j in range(l, w + 1):
            a = dp[j - l] + 1
            if a < dp[j]:
                dp[j] = a
        continue
    for r in range(l):
        old = dp[r::l]
        m = len(old)
        key = [v - i for i, v in enumerate(old)]
        dq = deque()
        for k in range(m):
            v = key[k]
            while dq and key[dq[-1]] >= v:
                dq.pop()
            dq.append(k)
            if dq[0] < k - c:
                dq.popleft()
            b = key[dq[0]] + k
            old[k] = b if b < BIG else BIG
        dp[r::l] = old

print(dp[w] if dp[w] < BIG else -1)