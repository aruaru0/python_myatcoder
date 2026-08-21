n, m = map(int, input().split())
t = [0] + list(map(int, input().split()))
for i in range(n) :
    t[i+1] += t[i]

for _ in range(m) :
    s, l, r = map(int, input().split())
    print(s + t[r] - t[l-1])