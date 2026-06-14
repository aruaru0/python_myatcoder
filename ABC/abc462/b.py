n = int(input())

b = [[] for _ in range(n)]
for i in range(n):
    s = list(map(int, input().split()))
    for e in s[1:] :
        b[e-1].append(i+1)


for e in b:
    print(len(e), *e)