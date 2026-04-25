N, M = map(int, input().split())
ivl = []
for _ in range(M):
    l, r = map(int, input().split())
    ivl.append((l, r))

ivl.sort()

mg = []
for l, r in ivl:
    if not mg or l > mg[-1][1] + 1:
        mg.append([l, r])
    else:
        mg[-1][1] = max(mg[-1][1], r)
        

pr = 0
for l, r in mg:
    gp = l - pr - 1
    if N <= gp:
        print(pr + N)
        exit()
    N -= gp
    pr = r
    
print(pr + N)

