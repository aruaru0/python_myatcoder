N, S, LL = map(int, input().split())
a = list(map(int, input().split()))


L = a[:S-1] + [0]
R = [0] + a[S-1:]


ans = 0
l = 0
for i, lv in enumerate(L[::-1]) :
    l += lv
    r = 0
    for j, rv in enumerate(R) :
        r += rv
        if l*2 + r <= LL or l + r*2 <= LL :
            ans = max(ans, i+j+1)

print(ans)