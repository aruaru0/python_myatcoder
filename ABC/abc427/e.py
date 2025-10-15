import collections

H, W = map(int, input().split())
S = [input().strip() for _ in range(H)]

t = -1    
mk = 0 
for i in range(H):
    row = S[i]
    for j, ch in enumerate(row):
        idx = i * W + j
        if ch == 'T':
            t = idx
        elif ch == '#':
            mk |= 1 << idx

nxt = [[-1] * (H * W) for _ in range(4)]
dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]   # 上 下 左 右
for d, (di, dj) in enumerate(dirs):
    for i in range(H):
        for j in range(W):
            cur = i * W + j
            ni, nj = i + di, j + dj
            if 0 <= ni < H and 0 <= nj < W:
                nxt[d][cur] = ni * W + nj  
            else:
                nxt[d][cur] = -1  

def trans(mask: int, d: int):
    nm = 0
    m = mask
    while m:
        lsb = m & -m
        idx = lsb.bit_length() - 1
        nd = nxt[d][idx]
        if nd == -1:
            pass
        else:
            if nd == t:
                return None
            nm |= 1 << nd
        m ^= lsb
    return nm

q = collections.deque()
q.append((mk, 0))
vis = {mk}
ans = -1

while q:
    mask, dist = q.popleft()
    if mask == 0:
        ans = dist
        break
    for d in range(4):
        nmask = trans(mask, d)
        if nmask is None:
            continue
        if nmask not in vis:
            vis.add(nmask)
            q.append((nmask, dist + 1))

print(ans)


