x, y, l, r, a, b = map(int, input().split())


h_x = max(0, min(b, r) - max(a, l))
h_y = b-a - h_x

print(h_x * x + h_y*y)