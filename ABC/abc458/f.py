from collections import deque

MOD = 998244353

# 入力
n, k = map(int, input().split())
s = [input().strip() for _ in range(k)]

# ACオートマトンの構築 (トライ木)
# nx: 遷移先, fl: 失敗リンク, fb: 禁止フラグ
nx = [[-1] * 26]
fl = [0]
fb = [False]

for st in s:
    u = 0
    for c in st:
        idx = ord(c) - 97
        if nx[u][idx] == -1:
            nx[u][idx] = len(nx)
            nx.append([-1] * 26)
            fl.append(0)
            fb.append(False)
        u = nx[u][idx]
    fb[u] = True

# 失敗リンクの計算と遷移関数の完成 (BFS)
qu = deque()
for i in range(26):
    if nx[0][i] != -1:
        qu.append(nx[0][i])
    else:
        nx[0][i] = 0  # ルートの欠けている遷移はルート自身へ

while qu:
    u = qu.popleft()
    # 失敗リンク先が禁止なら自身も禁止
    if fb[fl[u]]:
        fb[u] = True
    for i in range(26):
        if nx[u][i] != -1:
            fl[nx[u][i]] = nx[fl[u]][i]
            qu.append(nx[u][i])
        else:
            nx[u][i] = nx[fl[u]][i]  # 失敗リンク経由の遷移を埋める

# 有効な状態のみを残して再インデックス
va = [i for i in range(len(fb)) if not fb[i]]
mp = {old: new for new, old in enumerate(va)}
m = len(va)

# 遷移行列の構築
mt = [[0] * m for _ in range(m)]
for u in va:
    nu = mp[u]
    for i in range(26):
        v = nx[u][i]
        if not fb[v]:
            nv = mp[v]
            mt[nu][nv] += 1

# 行列乗算 (O(sz^3))
def mat_mul(A, B):
    sz = len(A)
    C = [[0] * sz for _ in range(sz)]
    for i in range(sz):
        for kk in range(sz):
            ai = A[i][kk]
            if ai == 0:
                continue
            bk = B[kk]
            ci = C[i]
            for j in range(sz):
                ci[j] += ai * bk[j]
        for j in range(sz):
            C[i][j] %= MOD
    return C

# 行列累乗 (O(sz^3 log p))
def mat_pow(A, p):
    sz = len(A)
    rs = [[0] * sz for _ in range(sz)]
    for i in range(sz):
        rs[i][i] = 1
    while p > 0:
        if p % 2 == 1:
            rs = mat_mul(rs, A)
        A = mat_mul(A, A)
        p //= 2
    return rs

# N 乗を計算
rs = mat_pow(mt, n)

# 初期状態（ルート）から始まる長さ N の経路の総和
ans = sum(rs[0]) % MOD
print(ans)

