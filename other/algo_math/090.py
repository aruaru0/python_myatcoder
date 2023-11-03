N, B = map(int, input().split())

def f(x):
    if x == 0:
        return 0
    
    res = 1
    while x > 0:
        res *= x % 10
        x //= 10
    return res
    

ans = 0
for a in range(100):
    if 2**a > 10**11 : continue
    for b in range(100):
        if 3**b > 10**11 : continue
        for c in range(100):
            if 5**c > 10**11 : continue
            for d in range(100):      
                if 7**d > 10**11 : continue
                fm = 2**a * 3**b * 5**c * 7**d
                # print(fm)
                m = fm + B
                if fm == f(m) and 1 <= m <= N:
                    ans += 1

fm = 0
m = fm + B
if fm == f(m) and 1 <= m <= N:
    ans += 1
    
print(ans)