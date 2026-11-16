n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

def check(a, b) :
    q = []
    ai = 0
    bi = 0
    flg = False
    while bi < len(b) :
        if a[ai] == b[bi] : 
            ai += 1
            bi += 1
            continue
        if len(q) != 0 and a[ai] == q[0] :
            q = q[1:]
            flg = True
            ai += 1
            continue
        q.append(b[bi])
        if len(q) > 1 or flg :
            return False
        bi+=1
    if ai != len(a) and len(q) != 0 and a[ai] != q[0] :
        return False
    return True

if check(a, b) or check(b, a) :
    print("Yes")
else:
    print("No")