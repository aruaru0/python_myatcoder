n_q = input().split()
while len(n_q) < 2:
    n_q += input().split()
n = int(n_q[0]); q = int(n_q[1])
xs = [0]*n
ys = [0]*n
for i in range(n):
    x_y = input().split()
    while len(x_y) < 2:
        x_y += input().split()
    xs[i] = int(x_y[0]); ys[i] = int(x_y[1])

N2 = 2*n
X = xs + xs
Y = ys + ys

pref_c = [0]*N2
pref_cx = [0]*N2
pref_cy = [0]*N2

for i in range(N2-1):
    cr = X[i]*Y[i+1] - X[i+1]*Y[i]
    pref_c[i+1] = pref_c[i] + cr
    pref_cx[i+1] = pref_cx[i] + (X[i]+X[i+1])*cr
    pref_cy[i+1] = pref_cy[i] + (Y[i]+Y[i+1])*cr

out = []
for _ in range(q):
    uv = input().split()
    while len(uv) < 2:
        uv += input().split()
    u = int(uv[0])-1
    v = int(uv[1])-1
    if v <= u:
        v += n
    sum_cross = pref_c[v] - pref_c[u]
    sum_cx = pref_cx[v] - pref_cx[u]
    sum_cy = pref_cy[v] - pref_cy[u]
    closing = X[v]*Y[u] - X[u]*Y[v]
    tot_cross = sum_cross + closing
    tot_cx = sum_cx + (X[v]+X[u])*closing
    tot_cy = sum_cy + (Y[v]+Y[u])*closing
    cx = tot_cx / (3.0 * tot_cross)
    cy = tot_cy / (3.0 * tot_cross)
    out.append(f"{cx:.15f} {cy:.15f}")

for line in out:
    print(line)
