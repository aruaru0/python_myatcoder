import math

N = int(input())
L = []
for i in range(N):
    X, Y = map(int, input().split())
    L.append((X, Y, i + 1))

B = int(20000000 / math.sqrt(N)) + 1

L.sort(key=lambda pt: (pt[0] // B, pt[1] if (pt[0] // B) % 2 == 0 else -pt[1]))

p1 = -1
for i, pt in enumerate(L):
    if pt[2] == 1:
        p1 = i
        break

ans = [pt[2] for pt in L[p1:] + L[:p1]]
print(*(ans))