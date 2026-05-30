g, m, d, k, v = map(int, input().split())

if d * k >= g:
    left = g * v
    right = d * (m - g)
else:
    left = v * (k + g - d * k)
    right = m - g

print("Yes" if left <= right else "No")
