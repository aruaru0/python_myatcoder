n, k = map(int, input().split())

a = list(map(int, input().split()))

mx, pos = a[0], 0

for i in range(n) :
    if mx < a[i] :
        pos = i
        mx = a[i]

print(pos+1)