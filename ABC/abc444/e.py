from sortedcontainers import SortedSet

n, d = map(int, input().split())
a = list(map(int, input().split()))

s = SortedSet()

inf = int(1e15)
s.add(-inf)
s.add(inf)
ans = 0
l = 0
for r in range(n) :
    while True:
        cur = s.bisect_left(a[r])
        if s[cur]-a[r] >= d and a[r]-s[cur-1] >= d :
            break
        s.remove(a[l])
        l += 1
    s.add(a[r])
    ans += r - l +1


print(ans)