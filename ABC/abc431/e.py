import sys
from collections import deque

inp = sys.stdin.readline
T = int(inp())
out = []

# 方向ベクトル (上,右,下,左)
dx = (-1, 0, 1, 0)
dy = (0, 1, 0, -1)

# 反射テーブル
rA = (0, 1, 2, 3)          # A : 何もしない
rB = (3, 2, 1, 0)          # B : '\'
rC = (1, 0, 3, 2)          # C : '/'

for _ in range(T):
    H, W = map(int, inp().split())
    s = [inp().strip() for __ in range(H)]

    INF = 10 ** 9
    N = H * W * 4                     # (i,j,d) の総数
    dist = [INF] * N

    # 開始状態：左側から右向きで (0,0) に入る
    st = ((0 * W + 0) << 2) | 1       # d=1(右)
    dist[st] = 0
    dq = deque([st])
    ans = INF

    while dq:
        v = dq.popleft()
        cur = dist[v]
        if cur >= ans:
            continue

        d = v & 3                     # 入る方向
        c = v >> 2                    # i*W + j
        i = c // W
        j = c % W

        # ----- タイプ A -----
        nd = rA[d]
        cost = 0 if s[i][j] == 'A' else 1
        ni = i + dx[nd]; nj = j + dy[nd]
        nc = cur + cost
        if not (0 <= ni < H and 0 <= nj < W):
            if i == H - 1 and j == W - 1 and nd == 1:
                if nc < ans:
                    ans = nc
        else:
            nid = ((ni * W + nj) << 2) | nd
            if nc < dist[nid]:
                dist[nid] = nc
                if cost == 0:
                    dq.appendleft(nid)
                else:
                    dq.append(nid)

        # ----- タイプ B -----
        nd = rB[d]
        cost = 0 if s[i][j] == 'B' else 1
        ni = i + dx[nd]; nj = j + dy[nd]
        nc = cur + cost
        if not (0 <= ni < H and 0 <= nj < W):
            if i == H - 1 and j == W - 1 and nd == 1:
                if nc < ans:
                    ans = nc
        else:
            nid = ((ni * W + nj) << 2) | nd
            if nc < dist[nid]:
                dist[nid] = nc
                if cost == 0:
                    dq.appendleft(nid)
                else:
                    dq.append(nid)

        # ----- タイプ C -----
        nd = rC[d]
        cost = 0 if s[i][j] == 'C' else 1
        ni = i + dx[nd]; nj = j + dy[nd]
        nc = cur + cost
        if not (0 <= ni < H and 0 <= nj < W):
            if i == H - 1 and j == W - 1 and nd == 1:
                if nc < ans:
                    ans = nc
        else:
            nid = ((ni * W + nj) << 2) | nd
            if nc < dist[nid]:
                dist[nid] = nc
                if cost == 0:
                    dq.appendleft(nid)
                else:
                    dq.append(nid)

    print(ans)


