N = int(input())
s = set(map(int, input().split()))


Q = int(input())
for _ in range(Q):
    m = int(input())
    t = list(map(int, input().split()))
    mt = set()
    for e in t :
        if e not in s :
            mt.add(e)
    print(len(mt)+len(s))