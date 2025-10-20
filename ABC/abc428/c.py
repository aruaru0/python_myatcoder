Q = int(input())
b = [0]
m = [0]
out = []
for _ in range(Q):
    cur = input().split()
    if cur[0] == '1':                     # push
        c = cur[1]
        nb = b[-1] + (1 if c == '(' else -1)
        nm = m[-1] if m[-1] < nb else nb  # min(m[-1], nb)
        b.append(nb)
        m.append(nm)
    else:                                 # pop
        b.pop()
        m.pop()
    print(b,m )
    out.append('Yes' if b[-1] == 0 and m[-1] >= 0 else 'No')
print('\n'.join(out))

