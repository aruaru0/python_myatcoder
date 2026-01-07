n = int(input())

a = [list(map(int, input().split())) for _ in range(n)]

a.sort(key=lambda x : (x[0], -x[1]))

inf = int(1e9+1)
dp = [inf] * n

def lower_bound(dp, x) :
    l, r = -1, len(dp)
    while l+1 != r :
        mid = (l+r) // 2
        if dp[mid] >= x :
            r = mid
        else :
            l = mid
    return r

for i in range(n) :
    pos = lower_bound(dp, a[i][1])
    dp[pos] = a[i][1]


ans = lower_bound(dp, inf)
print(ans)