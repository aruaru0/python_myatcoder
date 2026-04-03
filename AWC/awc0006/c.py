n, m, d = map(int, input().split())
t = list(map(int, input().split()))

tot = 0
for i in range(n):
    diff = max(0, t[i] - m)
    tot += (diff + d - 1) // d

print(tot)