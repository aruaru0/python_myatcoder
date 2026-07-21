t = int(input())
for _ in range(t):
    px, py, qx, qy, rx, ry, sx, sy = map(int, input().split())
    dx1 = qx - px
    dy1 = qy - py
    dx2 = sx - rx
    dy2 = sy - ry
    if dx1 * dy2 != dx2 * dy1:
        print("Yes")
    else:
        if dx2 * (px + qx) + dy2 * (py + qy) == sx * sx + sy * sy - rx * rx - ry * ry:
            print("Yes")
        else:
            print("No")
