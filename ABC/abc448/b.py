n,m = map(int, input().split())
c = list(map(int, input().split()))

tot = 0
for _ in range(n) :
    a, b = map(int, input().split())
    a -= 1
    d = min(c[a], b)
    c[a] -= d
    tot += d

print(tot)
