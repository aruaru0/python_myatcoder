n,m = map(int, input().split())


used = set()
for i in range(n) :
    l = int(input())
    x = list(map(int, input().split()))
    sel = 0
    for e in x :
        if e not in used :
            used.add(e)
            sel = e
            break
    print(sel)
    