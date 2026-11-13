Q = int(input())

p = set()
for _ in range(Q) :
    t, x = map(int, input().split())
    if t == 1 :
        p.add(x)
    else:
        if x in p :
            print("Yes")
        else:
            print("No")