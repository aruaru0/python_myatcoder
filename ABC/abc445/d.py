from collections import deque

H, W, N = map(int, input().split())

h = []
w = []
for i in range(N):
    x, y = map(int, input().split())
    h.append((x, y, i))
    w.append((x, y, i))

h.sort(key=lambda x:x[0], reverse=True)
w.sort(key=lambda x:x[1], reverse=True)

h = deque(h)
w = deque(w)



used = [False] * N
pos = [[]] * N

ph, pw = 0,0
for i in range(N) :
    while len(h) != 0 and used[h[0][2]] == True:
        h.popleft()
    while len(w) != 0 and used[w[0][2]] == True:
        w.popleft()

    if len(h)!=0 and h[0][0] == H :
        pos[h[0][2]] = (ph, pw)
        pw += h[0][1]
        used[h[0][2]] = True
        W -= h[0][1]
    elif len(w) != 0 and w[0][1] == W:
        pos[w[0][2]] = (ph, pw)
        ph += w[0][0]
        used[w[0][2]] = True
        H -= w[0][0]


for (x, y) in pos :
    print(x+1, y+1)
    
