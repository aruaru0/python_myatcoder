import sys

Q = 1 << 70

def akey(x, y):
    if y >= 0 and x > 0:
        return (0, y * Q // x)
    if x <= 0 and y > 0:
        return (1, -x * Q // y)
    if y <= 0 and x < 0:
        return (2, -y * Q // -x)
    return (3, x * Q // -y)


t = int(input())
out = []
for _ in range(t):
    n = int(input())
    pts = []
    for _ in range(n):
        x, y = map(int, input().split())
        pts.append((akey(x, y), x, y))
    pts.sort()
    a = [(x, y) for _, x, y in pts]
    a += a

    ans = 0
    j = 0
    for i in range(n):
        if j < i + 1:
            j = i + 1
        xi, yi = a[i]
        lim = i + n
        while j < lim:
            xj, yj = a[j]
            if xi * yj - yi * xj > 0:  
                j += 1
            else:
                break
        if j - i > ans:
            ans = j - i
    out.append(ans)

print("\n".join(map(str, out)))
