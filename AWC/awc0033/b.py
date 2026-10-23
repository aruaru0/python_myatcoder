n, k, l, r = map(int, input().split())
t = list(map(int, input().split()))

d = [0] * n 
for i in range(n):
    if t[i] < l :
        d[i] = l - t[i]
    elif t[i] > r :
        d[i] = t[i] - r

d.sort()

print(sum(d[:k]))