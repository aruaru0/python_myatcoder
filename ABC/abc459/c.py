n, q = map(int, input().split())


h = [0]*n
c = [0]*(10**6)

c[0] = n
l = 0
for _ in range(q) :
    t, x = map(int, input().split())
    if t == 1 :
        x -= 1
        h[x] += 1
        c[h[x]] += 1
        if (c[l+1] == n) :
            l += 1
    else :
        print(c[l+x]) 
    # print(h, c[:10])