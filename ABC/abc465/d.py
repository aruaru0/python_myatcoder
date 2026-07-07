import sys

T = int(input())
out = []
for _ in range(T):
    X, Y, K = map(int, input().split())

    if X == Y:
        print(0)
        continue

    x, y = X, Y
    dx = 0
    while x:
        x //= K
        dx += 1

    dy = 0
    while y:
        y //= K
        dy += 1

    x, y = X, Y
    ans = 0

    while dx > dy:
        x //= K
        dx -= 1
        ans += 1
    while dy > dx:
        y //= K
        dy -= 1
        ans += 1

    while x != y:
        x //= K
        y //= K
        ans += 2

    print(ans)
