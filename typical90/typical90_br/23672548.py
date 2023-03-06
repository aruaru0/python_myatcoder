# Contest ID: typical90
# Problem ID: typical90_br ( https://atcoder.jp/contests/typical90/tasks/typical90_br )
# Title: 070. Plant Planning（★4）
# Language: Python (3.8.2)
# Submitted: 2021-06-21 23:53:24 +0000 UTC ( https://atcoder.jp/contests/typical90/submissions/23672548 ) 

N = int(input())
x = [0]*N
y = [0]*N

for i in range(N):
    x[i], y[i] = map(int, input().split())

x.sort()
y.sort()

xc = x[N//2]
yc = y[N//2]
if N % 2 == 0:
    xc += x[N//2-1]
    yc += y[N//2-1]
    xc //= 2
    yc //= 2

tot = 0
for i in range(N):
    tot += abs(x[i]-xc) + abs(y[i]-yc)
print(tot)
