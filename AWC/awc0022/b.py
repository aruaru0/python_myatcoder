n, m, t = map(int, input().split())
a = list(map(int, input().split()))

tot = sum([max(0, t-e) for e in a])

if tot > m :
    print(-1)
else :
    print(tot)