n, m = map(int, input().split())

d, r = divmod(m, n)

for i in range(n) :
    if i < r :
        print(d+1)
    else:
        print(d)