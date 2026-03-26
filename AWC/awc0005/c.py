N, K = map(int, input().split())
A = list(map(int, input().split()))

# P[i] は、i までの範囲（左側）からの制約を考慮した時の最大値の基準
# 式：max(A[j] + K*j) for j <= i
P = [0] * N
for i in range(N):
    val = A[i] + K * i
    if i == 0:
        P[i] = val
    else:
        P[i] = max(P[i-1], val)

# S[i] は、i 以降の範囲（右側）からの制約を考慮した時の最大値の基準
# 式：max(A[j] - K*j) for j >= i
S = [0] * N
for i in range(N - 1, -1, -1):
    val = A[i] - K * i
    if i == N - 1:
        S[i] = val
    else:
        S[i] = max(S[i+1], val)

ans = 0
for i in range(N):
    # 各位置での最小必要花の本数
    term = max(P[i] - K * i, S[i] + K * i)
    ans += term - A[i]

print(ans)
