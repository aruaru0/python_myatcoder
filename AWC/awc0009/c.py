n, k, t = map(int, input().split())
h = list(map(int, input().split()))
mi = min(h) - 1

cnt = 0
for e in h:
    if e-mi <= t+k:
        cnt += 1

print(cnt)