n = int(input())

ribs = []
for _ in range(n):
    a, b = map(int, input().split())
    ribs.append((a, b))
    
m = int(input())

ss = []
for _ in range(m):
    ss.append(input())
    
v_set = set()

for s in ss:
    l = len(s)
    for i in range(l):
        v_set.add((l, i + 1, s[i]))

res = []
for s in ss:
    if len(s) != n:
        print("No")
        continue
    
    ok = True
    for i in range(n):
        a, b = ribs[i]
        if (a, b, s[i]) not in v_set:
            ok = False
            break
        
    if ok :
        print("Yes")
    else :
        print("No")

        

