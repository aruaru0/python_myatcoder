from collections import defaultdict

q = int(input())
m = defaultdict(int)

for _ in range(q):
    t = list(map(int, input().split()))
    if t[0] == 1 :
        m[t[1]]+=1
    elif t[0] == 2:
        m[t[1]]-=1
        if m[t[1]] == 0 :
            del m[t[1]]
    else:
        print(len(m))