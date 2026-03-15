h, w, q = map(int, input().split())

for _ in range(q):
    cmd = input().split()
    t = int(cmd[0])
    
    if t == 1:
        r = int(cmd[1])
        print(w * r) 
        h -= r
    else:
        c = int(cmd[1])
        print(h * c)
        w -= c
