n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

def f(off) :
    prev = a[0] + off
    cnt = off
    for i in range(1, n) :
        d = 0
        if b[i-1] == 0 :
            if prev%2 != a[i]%2 : d = 1
        else:
            if prev%2 == a[i]%2 : d = 1
        
        prev = a[i] + d
        cnt += d
    return cnt

print(min(f(0), f(1)))


