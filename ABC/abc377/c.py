n, m = map(int, input().split())

st = set()
for i in range(m) :
    y, x = map(int, input().split())
    x-=1
    y-=1

    st.add((x, y))
    for dx, dy in zip((1, 2, 2, 1, -1, -2, -2, -1), (2, 1, -1, -2, -2, -1, 1, 2)) :
        px, py = x+dx, y+dy
        if px < 0 or py < 0 or px >= n or py >= n :continue
        st.add((px, py))


print(n*n - len(st))