x = int(input())
n = int(input())
ws = list(map(int, input().split()))
q = int(input())

cur = x 
on = [False] * (n + 1) 
for _ in range(q):
    p = int(input())  
    if not on[p]: 
        cur += ws[p - 1]
        on[p] = True
    else: 
        cur -= ws[p - 1]
        on[p] = False
    print(cur)
