n,t = map(int, input().split())

tot = 0
for i in range(n):
    a, b = map(int, input().split())
    tot += max(a-b*t, 0)

print(tot)