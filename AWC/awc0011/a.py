n, m = map(int, input().split())
s, t = map(int, input().split())

if s > t :
    s, t = t, s


ans = 0
for _ in range(m):
    p, v = map(int, input().split())
    if s <= p <= t:
        ans += v
        
print(ans)

