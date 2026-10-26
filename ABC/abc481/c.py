q = int(input())

m = {}
for _ in range(q):
    s = input()
    if s not in m :
        m[s] = len(m)+1
    print(m[s])