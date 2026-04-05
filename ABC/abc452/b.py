h, w = map(int, input().split())
for r in range(h):
    s = ""
    for c in range(w):
        if r == 0 or r == h - 1 or c == 0 or c == w - 1:
            s += "#"
        else:
            s += "."
    print(s)
