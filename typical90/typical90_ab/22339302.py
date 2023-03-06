# Contest ID: typical90
# Problem ID: typical90_ab ( https://atcoder.jp/contests/typical90/tasks/typical90_ab )
# Title: 028. Cluttered Paper（★4）
# Language: Python (3.8.2)
# Submitted: 2021-05-06 00:54:33 +0000 UTC ( https://atcoder.jp/contests/typical90/submissions/22339302 ) 

N = int(input())

n = 1010

pos = [list(map(int, input().split())) for _ in range(N)]

c = [[0 for _ in range(n)] for _ in range(n)]

for e in pos:
    x0, y0, x1, y1 = e[0], e[1], e[2], e[3]
    c[y0][x0] += 1
    c[y0][x1] -= 1
    c[y1][x0] -= 1
    c[y1][x1] += 1


for y in range(1, n):
    for x in range(n):
        c[y][x] += c[y-1][x]

for x in range(1, n):
    for y in range(n):
        c[y][x] += c[y][x-1]


cnt = [0 for _ in range(N+1)]
for y in range(n):
    for x in range(n):
        cnt[c[y][x]] += 1

for i in range(1, N+1):
    print(cnt[i])
