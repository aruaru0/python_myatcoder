import sys


def solve():
    N, C = map(int, input().split())
    C -= 1                       # 0‑ベースへ

    grid = [list(input()) for _ in range(N)]

    # 壁の位置リストと top / idx の初期化
    walls = [[] for _ in range(N)]
    for i in range(N):
        row = grid[i]
        for j, ch in enumerate(row):
            if ch == '#':
                walls[j].append(i)

    idx  = [len(w) - 1 for w in walls]
    top  = [walls[j][idx[j]] if idx[j] >= 0 else -1 for j in range(N)]

    reach = [False] * N
    reach[C] = True

    # 下から上へ DP
    for rc in range(N - 1, 0, -1):
        a = rc - 1
        nxt = [False] * N
        for c in range(N):
            if not reach[c]:
                continue
            for b in (c - 1, c, c + 1):
                if b < 0 or b >= N:
                    continue
                if grid[a][b] == '.':
                    nxt[b] = True
                else: 
                    if top[b] <= a: 
                        nxt[b] = True
                        if top[b] == a:
                            idx[b] -= 1
                            top[b] = walls[b][idx[b]] if idx[b] >= 0 else -1
                            grid[a][b] = '.' 
        reach = nxt

    ans = ''.join('1' if reach[i] else '0' for i in range(N))
    print(ans)


T = int(input())
for _ in range(T) : 
    solve()
