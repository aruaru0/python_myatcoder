N,Q = map(int, input().split())

a = [0 for _ in range(N+1)]
for _ in range(Q) :
    l, r, x = map(int, input().split())
    l -= 1
    a[l] += x
    a[r] -= x

for i in range(N):
    a[i+1] += a[i]


ans = ""
for i in range(N-1):
    if a[i] > a[i+1] : ans += '>'
    elif a[i] == a[i+1] : ans += '='
    else: ans += '<'

print(ans)