from collections import deque

N, M = map(int, input().split())
S = [input() for _ in range(N)]

dist = [[10**9] * M for _ in range(N)]
dist[0][0] = 0
q = deque([(0, 0)])

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

while q:
    r, c = q.popleft()
    d = dist[r][c]
    for i in range(4):
        nr = r + dx[i]
        nc = c + dy[i]
        if 0 <= nr < N and 0 <= nc < M:
            w = 1 if S[nr][nc] == '#' else 0
            if dist[nr][nc] > d + w:
                dist[nr][nc] = d + w
                if w == 0:
                    q.appendleft((nr, nc))
                else:
                    q.append((nr, nc))

print(dist[N-1][M-1])
