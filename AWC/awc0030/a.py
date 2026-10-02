n, m = map(int, input().split())
a = list(map(int, input().split()))

for e in a :
    print(e//m, e%m)