n, q = map(int, input().split())
s = list(map(int, input().split()))

for _ in range(q) :
    a, b = map(int, input().split())
    a-=1
    b-=1
    if (s[a] > s[b]) :
        print("Yes")
    else:
        print("No")