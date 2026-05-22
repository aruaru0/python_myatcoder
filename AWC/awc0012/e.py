from collections import deque

n, k = map(int, input().split())
a = list(map(int, input().split()))

dp = [0] * n
dp[0] = a[0]

dq = deque()
dq.append(0)

for i in range(1, n):
    # ウィンドウ外（i-Kより左）のインデックスを削除
    while dq and dq[0] < i - k:
        dq.popleft()
    
    # 有効範囲内の最大DP値を持つインデックスは先頭
    dp[i] = a[i] + dp[dq[0]]
    
    # デックをDP値の降順に保つため、末尾から小さい値を削除
    while dq and dp[dq[-1]] <= dp[i]:
        dq.pop()
    dq.append(i)

print(dp[n-1])

