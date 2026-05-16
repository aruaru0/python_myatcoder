n, t = map(int, input().split())
h = list(map(int, input().split()))
c = list(map(int, input().split()))

cost = 0
for i in range(n):
    if h[i] <= t:
        cost += c[i]

print(cost)