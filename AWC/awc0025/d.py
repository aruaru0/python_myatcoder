import sys


N, S, Q = map(int, input().split())
S -= 1

# x: [(座標, 元のインデックス), ...]
x = [(e, i) for i, e in enumerate(list(map(int, input().split())))]
x.sort(key=lambda item: item[0])

# ダブリングテーブルの構築 (2^65 まで対応)
p = [[0] * N for _ in range(65)]

for i in range(N):
    if i == 0:
        p[0][i] = 1
        continue
    if i == N - 1:
        p[0][i] = N - 2
        continue

    l_val, li = x[i - 1]
    r_val, ri = x[i + 1]
    c_val, _ = x[i]

    dist_l = abs(c_val - l_val)
    dist_r = abs(c_val - r_val)

    if dist_l == dist_r:
        p[0][i] = i - 1 if li < ri else i + 1
    elif dist_l < dist_r:
        p[0][i] = i - 1
    else:
        p[0][i] = i + 1

for k in range(1, 65):
    p_prev = p[k - 1]
    p_curr = p[k]
    for j in range(N):
        p_curr[j] = p_prev[p_prev[j]]

# 開始位置のソート後インデックスを特定
cur = 0
for i in range(N):
    if x[i][1] == S:
        cur = i
        break

# ダブリングによる遷移
k = 0
while Q > 0:
    if Q & 1:
        cur = p[k][cur]
    Q >>= 1
    k += 1

# 1-indexed で出力
print(x[cur][1] + 1)


