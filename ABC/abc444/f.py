import sys

def solve() -> None:
    it = iter(sys.stdin.read().strip().split())
    t = int(next(it))
    out_lines = []
    for _ in range(t):
        N = int(next(it)); M = int(next(it))
        A = [int(next(it)) for _ in range(N)]
        L = N + M
        k = (L + 1) // 2          # median position

        maxA = max(A)

        def feasible(X: int) -> bool:
            cnt_ge = 0
            sum_t = 0
            for a in A:
                if a >= X:
                    cnt_ge += 1
                    n = a // X               # >= 1
                    t_val = n.bit_length() - 1   # floor(log2(n))
                    sum_t += t_val
            return cnt_ge + min(M, sum_t) >= k

        lo, hi = 1, maxA
        while lo < hi:
            mid = (lo + hi + 1) // 2
            if feasible(mid):
                lo = mid
            else:
                hi = mid - 1
        out_lines.append(str(lo))

    sys.stdout.write("\n".join(out_lines))

if __name__ == "__main__":
    solve()
