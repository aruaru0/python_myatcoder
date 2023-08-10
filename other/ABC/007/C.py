from collections import deque

R, C = map(int, input().split())

sy, sx = map(int, input().split())
gy, gx = map(int, input().split())
sy -= 1
sx -= 1
gy -= 1
gx -= 1

c = [input() for _ in range(R)]


inf = 10**9
dist = [[inf for _ in range(C)] for _ in range(R)]

dist[sy][sx] = 0
q = deque()
q.append((sx, sy))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
while len(q) != 0 :
    cx, cy = q[0]
    q.popleft()
    for i in range(4):
        px, py = cx + dx[i], cy + dy[i]
        if px < 0 or px >= C or py < 0 or py >= R : continue
        if c[py][px] == '#' : continue
        if dist[py][px] > dist[cy][cx] + 1:
            dist[py][px] = dist[cy][cx] + 1
            q.append((px, py))


print(dist[gy][gx])