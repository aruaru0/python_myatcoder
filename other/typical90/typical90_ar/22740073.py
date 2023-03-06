# Contest ID: typical90
# Problem ID: typical90_ar ( https://atcoder.jp/contests/typical90/tasks/typical90_ar )
# Title: 044. Shift and Swapping（★3）
# Language: Python (3.8.2)
# Submitted: 2021-05-19 23:12:58 +0000 UTC ( https://atcoder.jp/contests/typical90/submissions/22740073 ) 

N, Q = map(int, input().split())
a = list(map(int, input().split()))


offset = 0
for _ in range(Q):
    t, x, y = map(int, input().split())
    x = (x - 1 + offset + N) % N
    y = (y - 1 + offset + N) % N
    if t == 1:
        a[x], a[y] = a[y], a[x]
    elif t == 2:
        offset -= 1
    else:
        print(a[x])
