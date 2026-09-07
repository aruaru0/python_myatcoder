n = int(input())
a = list(map(int, input().split()))


b = []
for i in range(0, n, 10) :
    b += sorted(a[i:i+10])

ok = True
for i, e in enumerate(b):
    if i+1 != e :
        ok = False
        break


print("Yes" if ok else "No")