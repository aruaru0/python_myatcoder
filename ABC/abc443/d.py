t = int(input())


def solve() :
    n = int(input())
    a = list(map(int, input().split()))
    
    l = [0] * n
    r = [0] * n
    l[0], r[n-1] = a[0], a[n-1]

    for i in range(1, n):
        l[i] = min(a[i], l[i-1]+1)
    
    for i in range(n-2, -1, -1) :
        r[i] = min(a[i], r[i+1]+1)


    ans = sum(a[i]-min(l[i], r[i]) for i in range(n))

    print(ans)

for _ in range (t) :
    solve()