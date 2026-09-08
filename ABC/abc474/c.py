n, q = map(int, input().split())
p = list(map(int, input().split()))

a = [int(input()) for _ in range(q)]
a.reverse()

s = set()
b = []

for e in a:
    if e not in s :
        b.append(e)
        s.add(e)


ans = []
for e in p:
    if e not in s :
        ans.append(e)

b.reverse()
for e in b:
    ans.append(e)

print(*ans)