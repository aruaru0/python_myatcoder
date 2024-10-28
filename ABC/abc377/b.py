s = [input() for _ in range(8)]

h = [False] * 8
w = [False] * 8
for i in range(8) :
    for j in range(8) :
        if s[i][j] == '#' :
            h[i] = True
            w[j] = True

ans = 8*8
for i in range(8):
    for j in range(8) :
        if h[i] or w[j] :
            ans -=1

print(ans)