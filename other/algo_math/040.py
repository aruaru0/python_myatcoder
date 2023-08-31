N = int(input())

a = list(map(int, input().split()))
p = [0 for _ in range(N)]
for i in range(N-1):
    p[i+1] = a[i] + p[i]

M = int(input())
tot = 0
prev = -1
for _ in range(M):
    nxt = int(input()) - 1
    if prev != -1 :
        diff = abs(p[prev]-p[nxt])
        tot += diff
    prev = nxt

print(tot)