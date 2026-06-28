H, W = map(int, input().split())
C = [input() for _ in range(H)]
t, b = H, -1
l, r = W, -1
for i in range(H):
    for j in range(W):
        if C[i][j] == "#":
            t, b = min(t, i), max(b, i)
            l, r = min(l, j), max(r, j)
            
for i in range(t, b + 1):
    print(C[i][l:r+1])
