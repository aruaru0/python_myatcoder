from collections import Counter


T = int(input())
out = []
for _ in range(T):
    S = input().strip()
    N = len(S)
    cnt = Counter(S)
    chars = sorted(cnt.items(), key=lambda x: -x[1])
    if chars[0][1] > (N + 1) // 2:
        out.append("No")
    else:
        res = [''] * N
        idx = 0
        for c, f in chars:
            for _ in range(f):
                res[idx] = c
                idx += 2
                if idx >= N:
                    idx = 1
        out.append("Yes\n" + "".join(res))
print("\n".join(out))

