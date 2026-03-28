n, k, t = map(int, input().split())

tot = 0
for i in range(n):
    d, r = map(int, input().split())
    if r >= k*d:
        tot += r

if tot >= t:
    print("Yes")
else:
    print("No")