n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

for e in b :
    e -= 1
    for j in range(-1, 2):
        pos = e+j
        if 0 <= pos < n :
            a[pos]+=1


print(*a)   
