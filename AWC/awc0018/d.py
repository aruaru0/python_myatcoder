import sys


N, K = map(int, input().split())
prices = list(map(int, input().split()))

# dp[s] = True if sum s is achievable
dp = [False] * (K + 1)
dp[0] = True

for c in prices:
    # Iterate backwards to ensure each item is used at most once
    for s in range(K, c - 1, -1):
        if dp[s - c]:
            dp[s] = True

# Find the maximum achievable sum <= K
ans = 0
for s in range(K, -1, -1):
    if dp[s]:
        ans = s
        break

print(ans)

