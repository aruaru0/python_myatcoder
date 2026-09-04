from atcoder.segtree import SegTree

n = int(input())
s = list(input().strip())
q = int(input())


def op(a, b):
    sa, ma = a
    sb, mb = b
    return (sa + sb, min(ma, sa + mb))


v = []
for ch in s:
    x = 1 if ch == 'A' else -1
    v.append((x, min(0, x)))
seg = SegTree(op, (0, 0), v)

out = []
for _ in range(q):
    p = input().split()
    if p[0] == '1':
        i = int(p[1]) - 1
        c = p[2]
        if s[i] != c:
            s[i] = c
            x = 1 if c == 'A' else -1
            seg.set(i, (x, min(0, x)))
    else:
        l = int(p[1]) - 1
        r = int(p[2])
        out.append("Yes" if seg.prod(l, r)[1] >= 0 else "No")
print("\n".join(out))