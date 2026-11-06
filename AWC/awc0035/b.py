from bisect import bisect_left

n, m = map(int, input().split())
d = list(map(int, input().split()))
s = list(map(int, input().split()))
inf = 10**18
s.append(inf)
s.append(-inf)
s.sort()

ans = 0
for e in d :
    pos = bisect_left(s, e)
    ans += min(abs(s[pos] - e), abs(s[pos-1] - e))

print(ans)