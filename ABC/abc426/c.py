import sys
sys.setrecursionlimit(1 << 25)

N, Q = map(int, input().split())
# 配列は 0 番目をダミーにして 1-index にする
p = list(range(N + 2))
sz = [1] * (N + 2) 

def f(x: int) -> int:
    while p[x] != x:
        p[x] = p[p[x]]
        x = p[x]
    return x

out = []
for _ in range(Q):
    X, Y = map(int, input().split())
    cnt = 0
    v = f(X)
    ny = f(Y)                    # Y の根は変わらないので最初に取得しておく
    while v > 0 and v <= X:
        cnt += sz[v]
        p[v] = ny                # 統合
        sz[ny] += sz[v]
        v = f(v - 1)             # 次の候補へ
    out.append(str(cnt))
print("\n".join(out))


