n = int(input())
a = list(map(int, input().split()))


sel = 0
for i, e in enumerate(a) :
    if e > a[sel] :
        sel = i

if sel == 0 :
    print(-1)
else :
    print(sel+1)