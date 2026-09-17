import numpy as np

H, W = map(int, input().split())
rows = [input().strip() for _ in range(H)]

G = (np.frombuffer("".join(rows).encode(), dtype=np.uint8) == 46).reshape(H, W)

if W > H:
    G = np.ascontiguousarray(G.T)
    H, W = W, H

i32 = np.int32
col_idx = np.tile(np.arange(W, dtype=i32), (H, 1))
R = np.minimum.accumulate(np.where(G, col_idx, i32(W))[:, ::-1], axis=1)[:, ::-1]
R = np.ascontiguousarray(R)

row_idx = np.tile(np.arange(H, dtype=i32).reshape(H, 1), (1, W))
C = np.minimum.accumulate(np.where(G, row_idx, i32(H))[::-1, :], axis=0)[::-1, :]
C = np.ascontiguousarray(C)

CT = np.ascontiguousarray(C.T)
u = np.arange(H, dtype=i32)

total = 0
for l in range(W):
    Rl = R[:, l]  
    Cl = C[:, l]    
    rvec = np.arange(l, W, dtype=i32)
    B = Rl[None, :] <= rvec[:, None]
    cs = np.cumsum(B[:, ::-1], axis=1, dtype=i32)[:, ::-1]
    lo = np.maximum(CT[l:W, :], Cl[None, :]) 
    np.maximum(lo, u[None, :], out=lo)      
    idx = np.minimum(lo, H - 1).astype(np.intp)
    gath = np.take_along_axis(cs, idx, axis=1)
    gath[lo >= H] = 0
    total += int(np.where(B, gath, 0).sum(dtype=np.int64))

print(total + 1)
