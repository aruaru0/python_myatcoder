import sys

input = sys.stdin.readline

N_X_Y = input().split()
while len(N_X_Y) < 3:
    N_X_Y += input().split()
N, X, Y = map(int, N_X_Y)

C = []
A = []
B = []
for _ in range(N):
    parts = input().split()
    while len(parts) < 3:
        parts += input().split()
    c, a, b = parts[0], int(parts[1]), int(parts[2])
    C.append(c)
    A.append(a)
    B.append(b)

rects = []                     # (x1,x2,y1,y2) inclusive

# --------------------------------------------------------
# enumerate all sign patterns
for mask in range(1 << N):
    Lx, Rx = 0, X - 1
    Ly, Ry = 0, Y - 1
    cur_dx = 0                 # translation of x produced by processed Y‑storms
    cur_dy = 0                 # translation of y produced by processed X‑storms
    ok = True

    for i in range(N):
        sign = 1 if (mask >> i) & 1 else -1   # +1 : >= side , -1 : < side
        if C[i] == 'X':
            # condition uses current x = x0 + cur_dx
            if sign == -1:                     # x < A_i
                bound = A[i] - 1 - cur_dx
                if Rx > bound:
                    Rx = bound
            else:                              # x >= A_i
                bound = A[i] - cur_dx
                if Lx < bound:
                    Lx = bound
            cur_dy += sign * B[i]               # translation of y
        else:  # 'Y'
            # condition uses current y = y0 + cur_dy
            if sign == -1:                     # y < A_i
                bound = A[i] - 1 - cur_dy
                if Ry > bound:
                    Ry = bound
            else:                              # y >= A_i
                bound = A[i] - cur_dy
                if Ly < bound:
                    Ly = bound
            cur_dx += sign * B[i]               # translation of x

        if Lx > Rx or Ly > Ry:
            ok = False
            break

    if not ok:
        continue

    # final rectangle after the whole translation
    x1 = Lx + cur_dx
    x2 = Rx + cur_dx
    y1 = Ly + cur_dy
    y2 = Ry + cur_dy
    if x1 <= x2 and y1 <= y2:
        rects.append((x1, x2, y1, y2))

# --------------------------------------------------------
# coordinate compression
xs_set = set()
ys_set = set()
for x1, x2, y1, y2 in rects:
    xs_set.add(x1)
    xs_set.add(x2 + 1)          # half‑open border
    ys_set.add(y1)
    ys_set.add(y2 + 1)

xs = sorted(xs_set)
ys = sorted(ys_set)
nx = len(xs)
ny = len(ys)
xid = {v: i for i, v in enumerate(xs)}
yid = {v: i for i, v in enumerate(ys)}

# 2‑D difference array
diff = [[0] * ny for _ in range(nx)]
for x1, x2, y1, y2 in rects:
    i1 = xid[x1]
    i2 = xid[x2 + 1]
    j1 = yid[y1]
    j2 = yid[y2 + 1]

    diff[i1][j1] += 1
    diff[i2][j1] -= 1
    diff[i1][j2] -= 1
    diff[i2][j2] += 1

# prefix sums: first over x, then over y (2‑D imos)
for i in range(1, nx):
    row = diff[i]
    prev = diff[i - 1]
    for j in range(ny):
        row[j] += prev[j]

for i in range(nx):
    acc = 0
    row = diff[i]
    for j in range(ny):
        acc += row[j]
        row[j] = acc

# --------------------------------------------------------
# BFS on the compressed grid to obtain component sizes
visited = [bytearray(ny - 1) for _ in range(nx - 1)]
comp_sizes = []

for i in range(nx - 1):
    row_cov = diff[i]
    for j in range(ny - 1):
        if row_cov[j] <= 0 or visited[i][j]:
            continue
        # start a new component
        stack = [(i, j)]
        area = 0
        while stack:
            ci, cj = stack.pop()
            if visited[ci][cj]:
                continue
            visited[ci][cj] = 1
            area += (xs[ci + 1] - xs[ci]) * (ys[cj + 1] - ys[cj])

            # four neighbours
            ni = ci - 1
            if ni >= 0 and diff[ni][cj] > 0 and not visited[ni][cj]:
                stack.append((ni, cj))
            ni = ci + 1
            if ni < nx - 1 and diff[ni][cj] > 0 and not visited[ni][cj]:
                stack.append((ni, cj))
            nj = cj - 1
            if nj >= 0 and diff[ci][nj] > 0 and not visited[ci][nj]:
                stack.append((ci, nj))
            nj = cj + 1
            if nj < ny - 1 and diff[ci][nj] > 0 and not visited[ci][nj]:
                stack.append((ci, nj))

        comp_sizes.append(area)

comp_sizes.sort()
print(len(comp_sizes))
if comp_sizes:
    print(' '.join(str(v) for v in comp_sizes))
else:
    print()

