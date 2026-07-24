from collections import defaultdict

n,m,s = map(int, input().split())
d = list(map(int, input().split()))

r = defaultdict(int)
for _ in range(m) :
    a, b = map(int, input().split())
    r[a-1] = b


flg = False
for i in range(n):
    if flg :
        s -= d[i]*2
    else:
        s -= d[i]
    if s <= 0 :
        flg = True
    s += r[i]

print(s)