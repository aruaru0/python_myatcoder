n, t = map(int, input().split())

tot = 0
for _ in range(n):
    a, c = map(int, input().split())
    tot += max(0, (t-a)*c)

print(tot)