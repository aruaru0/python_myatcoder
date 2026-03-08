n, x = map(int, input().split())
a = list(map(int, input().split()))

for e in a :
    if (e < x) :
        x = e
        print(1)
    else :
        print(0)