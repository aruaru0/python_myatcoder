import sys
import math

def solve() -> None:
    it = iter(sys.stdin.read().strip().split())
    T = int(next(it))
    out_lines = []
    for _ in range(T):
        tsx = float(next(it)); tsy = float(next(it))
        tgx = float(next(it)); tgy = float(next(it))
        asx = float(next(it)); asy = float(next(it))
        agx = float(next(it)); agy = float(next(it))

        # vectors
        dx1 = tgx - tsx
        dy1 = tgy - tsy
        L1 = math.hypot(dx1, dy1)
        ux1 = dx1 / L1
        uy1 = dy1 / L1

        dx2 = agx - asx
        dy2 = agy - asy
        L2 = math.hypot(dx2, dy2)
        ux2 = dx2 / L2
        uy2 = dy2 / L2

        cand = [0.0, L1, L2]

        # interval I0 : both moving
        a0x = tsx - asx
        a0y = tsy - asy
        b0x = ux1 - ux2
        b0y = uy1 - uy2
        bb = b0x * b0x + b0y * b0y
        if bb > 0.0:
            t = -(a0x * b0x + a0y * b0y) / bb
            m = min(L1, L2)
            if 0.0 <= t <= m:
                cand.append(t)

        # interval where one has already stopped
        if L1 < L2 - 1e-12:          # I1 : Takahashi stopped
            a1x = tgx - asx
            a1y = tgy - asy
            b1x = -ux2
            b1y = -uy2
            bb = b1x * b1x + b1y * b1y
            if bb > 0.0:
                t = -(a1x * b1x + a1y * b1y) / bb
                if L1 <= t <= L2:
                    cand.append(t)
        elif L2 < L1 - 1e-12:        # I2 : Aoki stopped
            a2x = tsx - agx
            a2y = tsy - agy
            b2x = ux1
            b2y = uy1
            bb = b2x * b2x + b2y * b2y
            if bb > 0.0:
                t = -(a2x * b2x + a2y * b2y) / bb
                if L2 <= t <= L1:
                    cand.append(t)

        best_sq = float('inf')
        for t in cand:
            # position of Takahashi
            if t <= L1:
                p1x = tsx + ux1 * t
                p1y = tsy + uy1 * t
            else:
                p1x = tgx
                p1y = tgy
            # position of Aoki
            if t <= L2:
                p2x = asx + ux2 * t
                p2y = asy + uy2 * t
            else:
                p2x = agx
                p2y = agy

            dx = p1x - p2x
            dy = p1y - p2y
            d2 = dx * dx + dy * dy
            if d2 < best_sq:
                best_sq = d2

        out_lines.append("{:.15f}".format(math.sqrt(best_sq)))
    sys.stdout.write("\n".join(out_lines))

if __name__ == "__main__":
    solve()
