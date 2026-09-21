n = int(input())
a = list(map(int, input().split()))

b = []
for i in range(n):
    b.append(a[i])
    b.sort(reverse=True)
    b = b[:3]
    if len(b) == 3 :
        print(b[2])