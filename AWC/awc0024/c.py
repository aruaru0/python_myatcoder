from collections import defaultdict

H, W = map(int, input().split())

g = [input() for _ in range(H)]

h = [defaultdict(int) for _ in range(H)]
w = [defaultdict(int) for _ in range(W)]

for r in range(H) :
    for c in range(W) :
        ch = g[r][c]
        h[r][ch]+=1
        w[c][ch]+=1



ans = ""
for r in range(H) :
    for c in range(W) :
        ch = g[r][c]
        if h[r][ch] == 1 and w[c][ch] == 1 :
            ans += ch

print(ans)