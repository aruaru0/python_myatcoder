
def solve() :
    n, w = map(int, input().split())
    
    m = 2*w
    c = [0]*m
    x = list(map(int, input().split()))
    for i in range(1, n+1) :
        c[i%m] += x[i-1]

    cur = sum(c[:w])
    ans = cur
    for i in range(0,m) :
        cur -= c[i]
        cur += c[(i+w)%m]
        ans = min(ans, cur)
    print(ans)


t = int(input())
for _ in range(t):
    solve()