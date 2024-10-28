H, W = map(int, input().split())

s = [input() for _ in range (H)]
t = [input() for _ in range (H)]


ok = True
for i in range(H):
    a, b = 0,0
    for j in range(W):
        if s[i][j] == '#' : a+=1
        if t[i][j] == '#' : b+=1

    if a!=b : 
        ok = False
        break

if ok :
    print("Yes")
else:
    print("No")