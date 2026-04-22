def solve():
    N, A, B = map(int, input().split())
    a = A - 1
    b = B - 1
    
    if N % 2 != 0 or (a + b) % 2 == 0:
        print("No")
        return
    
    print("Yes")
    
    h = N
    w = N
    s_path = ""
    t_path = ""
    
    while True:
        if a >= 2:
            s_path += 'R' * (w - 1) + 'D' + 'L' * (w - 1) + 'D'
            h -= 2
            a -= 2
        elif a < h - 2:
            t_path += 'R' * (w - 1) + 'D' + 'L' * (w - 1) + 'D'
            h -= 2
        elif b >= 2:
            s_path += 'D' * (h - 1) + 'R' + 'U' * (h - 1) + 'R'
            w -= 2
            b -= 2
        elif b < w - 2:
            t_path += 'D' * (h - 1) + 'R' + 'U' * (h - 1) + 'R'
            w -= 2
        else:
            if a == 0:
                s_path += "DR"
            else:
                s_path += "RD"
            break
        
    t_rev = t_path[::-1]
    
    print(s_path + t_rev)


T = int(input())
for _ in range(T) :
    solve()