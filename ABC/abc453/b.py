T, X = map(int, input().split())

a = list(map(int, input().split()))

x = -10000
for i, e in enumerate(a) :
    if abs(e-x)>= X:
        x = e
        print(i, x)