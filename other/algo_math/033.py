ax, ay = map(int, input().split())
bx, by = map(int, input().split())
cx, cy = map(int, input().split())


def calc_vector(x0, y0, x1, y1) :
    return x1-x0, y1-y0

def calc_dist(dot, line):
    ax, ay = dot
    bx, by, cx, cy = line 
    BAx, BAy = calc_vector(bx, by, ax, ay)
    BCx, BCy = calc_vector(bx, by, cx, cy)
    CAx, CAy = calc_vector(cx, cy, ax, ay)
    CBx, CBy = calc_vector(cx, cy, bx, by)

    if BAx * BCx + BAy * BCy < 0 :
        return (BAx * BAx + BAy * BAy)**0.5
    if CAx * CBx + CAy * CBy < 0 :
        return (CAx * CAx + CAy * CAy)**0.5
    
    s = abs(BAx * BCy - BAy * BCx)
    l = (BCx*BCx + BCy * BCy)**0.5
    return s/l

dist = calc_dist((ax, ay), (bx, by, cx, cy))

print(dist)