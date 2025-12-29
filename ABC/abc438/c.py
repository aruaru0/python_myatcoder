n = int(input())
a = list(map(int, input().split()))

b = []
for e in a:
    b.append(e)
    if len(b) < 4 : continue
    if b[-1] == b[-2] == b[-3] == b[-4]:
        b.pop()
        b.pop()
        b.pop()
        b.pop()

print(len(b))
