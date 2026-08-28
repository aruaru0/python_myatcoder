h, w, n = map(int, input().split())

s = [list(input()) for _ in range(h)]

tot = 0
for e in s :
    tot += e.count('#')

cx, cy = 0,0
if s[cy][cx] == '#' :
    s[cy][cx] = '.' 
    tot-=1


t = input()
for e in t :
    nx, ny = cx, cy 
    if e == 'U' : ny-=1
    if e == 'D' : ny+=1
    if e == 'L' : nx-=1
    if e == 'R' : nx+=1
    if nx < 0 or nx >= w or ny < 0 or ny >= h :
        continue

    if s[ny][nx] == '#' :
        s[ny][nx] = '.'
        tot-=1

    cx, cy = nx, ny

print(tot)