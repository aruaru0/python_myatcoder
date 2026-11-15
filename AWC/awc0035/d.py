from functools import cmp_to_key

n, m = map(int, input().split())
v = list(map(int, input().split()))

w = [list(map(int, input().split())) for _ in range(m)]


def cmp(item1, item2) :
    x1, y1 = item1
    x2, y2 = item2
    return x1*y2 - x2*y1


v.sort()
w.sort(key=cmp_to_key(cmp))

cnt = 0
idx = 0
for [d, t] in w :
    while idx < n and v[idx]*t < d :
        idx+=1
    if idx == n : break
    cnt+=1
    idx+=1

print(cnt)
